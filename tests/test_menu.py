"""Test wechat custom menu module."""

from unittest import TestCase
from unittest.mock import patch

from wechatkit.exceptions import WechatException
from wechatkit.menu import (
    MenuUtil, MenuButton, ClickButton, ViewButton, SubButton,
    ScanButton, PhotoButton, LocationButton, MediaButton
)


class MenuUtilTest(TestCase):
    """MenuUtilTest test case."""

    def setUp(self):
        """Init setup."""

    def tearDown(self):
        """Tear down."""

    @patch('wechatkit.utils.RequestUtil.get')
    def test_query(self, mock_data):
        """Test query custom menu."""
        mock_data.return_value = {
            "menu": {
                "button": [{
                    "type": "click",
                    "name": "今日歌曲",
                    "key": "V1001_TODAY_MUSIC",
                    "sub_button": []
                }]
            }
        }
        resp = MenuUtil.query('access token')
        self.assertEqual(len(resp['menu']['button']), 1)

    def test_create_with_failure(self):
        """Test create custom menu."""
        resp = MenuUtil.create('test', 'access_token')
        self.assertEqual(resp['errcode'], 40001)

    @patch('wechatkit.utils.RequestUtil.post')
    def test_create_with_success(self, mock_data):
        """Test create custom menu success."""
        menu = {
            "button": [{
                "type": "click",
                "name": "今日歌曲",
                "key": "V1001_TODAY_MUSIC",
                "sub_button": []
            }]
        }
        mock_data.return_value = {
            "errcode": 0,
            "errmsg": "ok"
        }
        resp = MenuUtil.create(menu, 'access_token')
        self.assertEqual(resp['errcode'], 0)

    @patch('wechatkit.utils.RequestUtil.get')
    def test_delete(self, mock_data):
        """Test delete custom menu."""
        mock_data.return_value = {
            "errcode": 0,
            "errmsg": "ok"
        }
        resp = MenuUtil.delete('access_token')
        self.assertEqual(resp['errcode'], 0)


class MenuButtonTest(TestCase):
    """MenuButtonTest test case."""

    def setUp(self):
        """Init."""
        self.menu = MenuButton()

    def tearDown(self):
        """Tear down."""

    def test_menu_json(self):
        """Test menu json. """
        self.assertEqual(self.menu.json(), {'button': []})

    def test_menu_with_sub_button(self):
        """Test menu json with sub button. """
        click = ClickButton('测试', key='test')
        self.menu.add(click)
        self.assertIn(click.json(), self.menu.json()['button'])

    def test_menu_parse(self):
        """Test menu parse from json. """
        data = {'button': [{'key': 'test', 'name': '测试', 'type': 'click'}]}
        self.menu.parse(data)
        self.assertEqual(len(self.menu.buttons), 1)

    def test_menu_more_buttons(self):
        """Test menu more than 3 button. """
        click = ClickButton('测试', 'test')
        self.menu.add(click)
        self.menu.add(click)
        self.menu.add(click)
        with self.assertRaises(WechatException) as error:
            self.menu.add(click)

        self.assertEqual(
            error.exception.error_info, 'Level menu must not more than 3'
        )

    def test_menu_button_deep(self):
        """Test menu button with two deep. """
        sub = SubButton('导航')
        click = ClickButton('测试点击', 'click')
        view = ViewButton('测试视图', 'view')
        sub.add(click)
        sub.add(view)
        self.menu.add(sub)

        self.assertEqual(len(self.menu.buttons), 1)
        self.assertIn(
            click.json(),
            self.menu.json()['button'][0]['sub_button']
        )

    def test_sub_button_more(self):
        """ Test add more than 5 secondary button. """
        sub = SubButton('测试')
        click = ClickButton('测试', 'test')
        sub.add(click)
        sub.add(click)
        sub.add(click)
        sub.add(click)
        sub.add(click)
        with self.assertRaises(WechatException) as error:
            sub.add(click)

        self.assertEqual(
            error.exception.error_info, 'Secondary submenu must not more than 5'
        )

    def test_other_button(self):
        """ Test other button. """
        sub = SubButton('测试')
        scan = ScanButton('扫描', 'scan')
        sub.add(scan)
        photo = PhotoButton('相册', 'photo')
        sub.add(photo)
        loc = LocationButton('位置', 'location')
        sub.add(loc)
        media = MediaButton('图文', 'media_id')
        sub.add(media)
        self.menu.add(sub)

        self.assertEqual(len(self.menu.buttons[0].buttons), 4)

    def test_menu_button_parse(self):
        """ Test menu button parse. """
        data = {
            "button": [
                {
                    "type": "view",
                    "name": "我要吃饭",
                    "url": "test",
                    "sub_button": []
                }, {
                    "name": "订单",
                    "sub_button": [
                        {
                            "type": "view",
                            "name": "我的订单",
                            "url": "test..."
                        },
                        {
                            "type": "view",
                            "name": "我的收藏",
                            "url": "test..."
                        },
                        {
                            "type": "view",
                            "name": "优惠/折扣券",
                            "url": "test..."
                        }
                    ]
                },
                {
                    "name": "食饭志\"说\"",
                    "sub_button": [
                        {
                            "name": "成为\"料理人\"",
                            "type": "view",
                            "url": "test..."
                        },
                        {
                            "name": "关于\"食饭志\"",
                            "type": "view",
                            "url": "test..."
                        },
                        {
                            "name": "联系我们",
                            "type": "view",
                            "url": "test..."
                        }
                    ]
                }
            ]
        }
        self.menu.parse(data)

        self.assertEqual(len(self.menu.buttons), 3)
        self.assertEqual(len(self.menu.buttons[1].buttons), 3)
        self.assertEqual(self.menu.buttons[1].name, '订单')

    def test_no_value_button(self):
        """ Test no name for sub button. """
        with self.assertRaises(WechatException) as error:
            SubButton()

        self.assertEqual(error.exception.error_info, 'Not empty for `name`')

    def test_remove_menu_button(self):
        """ Test Remove menu button. """
        with self.assertRaises(WechatException) as error:
            self.menu.remove(1)

        self.assertEqual(error.exception.error_info, 'Sub button not exists')

        with self.assertRaises(WechatException) as error:
            sub = SubButton('test')
            sub.remove(1)

        self.assertEqual(error.exception.error_info, 'Sub button not exists')

    def test_remove_menu(self):
        """ Test Remove menu. """
        sub = SubButton('测试')
        click = ClickButton('测试', 'test')
        sub.add(click)
        self.menu.add(sub)

        self.assertEqual(click, sub.remove())
        self.assertEqual(sub, self.menu.remove())
