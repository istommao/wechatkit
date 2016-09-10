"""Test wechat custom menu module."""

from unittest import TestCase
from unittest.mock import patch

from wechatkit.menu import MenuUtil


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
