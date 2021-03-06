"""Test wechat payment module."""

from unittest import TestCase
from unittest.mock import patch

from wechatkit.exceptions import WechatKitException
from wechatkit.payment import WechatPay


class WechatPayTest(TestCase):
    """WechatPayTest test case."""

    def setUp(self):
        """Init setup."""
        self.appid = 'appid'
        self.pay = WechatPay(self.appid, 'mch_id', 'key')
        self.data = ''

    def tearDown(self):
        """Tear down."""

    def get_data(self):
        """Create dummy order data."""
        self.data = {
            'title': 'title',
            'order_uid': 'order_uid',
            'total': 10,
            'notify_url': 'notify_url',
            'trade_type': 'JSAPI',
            'ip': '127.0.0.1',
            'detail': 'test detail',
            'time_expire': 'now + 30m',
            'time_start': 'now',
            'product_id': 1
        }
        return self.data

    @patch('wechatkit.utils.RequestUtil.post_xml')
    def test_close_order(self, mock):
        """Test close order."""
        mock_data = {
            'return_code': 'SUCCESS',
            'return_msg': 'OK',
            'appid': self.appid
        }
        mock.return_value = mock_data
        dataset = {
            'order_uid': '12312321321'
        }
        result = self.pay.close_order(**dataset)
        self.assertEqual(result, mock_data)

    @patch('wechatkit.utils.RequestUtil.post_xml')
    def test_close_order_failure(self, mock):
        """Test close order."""
        mock_data = {
            'return_code': 'FAIL',
            'return_msg': '签名失败'
        }
        mock.return_value = mock_data

        dataset = {
            'order_uid': '12312321321'
        }
        with self.assertRaises(WechatKitException) as error:
            self.pay.close_order(**dataset)

        self.assertEqual(error.exception.error_info, '签名失败')

    @patch('wechatkit.utils.RequestUtil.post_xml')
    def test_create_order(self, mock_data):
        """Test create a wechat order."""
        mock_data.return_value = {'name': 'test', 'return_code': 'SUCCESS'}
        data = self.get_data()
        resp = self.pay.create_order('openid', **data)

        self.assertEqual(resp['name'], 'test')

    @patch('wechatkit.utils.RequestUtil.post_xml')
    def test_create_order_failure(self, mock_data):
        """Test create order failure."""
        mock_data.return_value = {
            'return_msg': 'test', 'return_code': 'FAILURE'
        }
        data = self.get_data()
        with self.assertRaises(WechatKitException) as error:
            self.pay.create_order('openid', **data)

        self.assertEqual(error.exception.error_info, 'test')

    def test_create_order_check_data(self):
        """Test check create order data."""
        data = self.get_data()
        data['title'] = ''
        with self.assertRaises(WechatKitException) as error:
            self.pay.create_order('openid', **data)

        self.assertEqual(error.exception.error_info, '订单描述不能为空')

        data['title'] = 'title'
        with self.assertRaises(WechatKitException) as error:
            self.pay.create_order(None, **data)

        self.assertEqual(error.exception.error_info, '用户标识不能为空')

        data['trade_type'] = self.pay.PAYMENT_NATIVE
        data['product_id'] = ''
        with self.assertRaises(WechatKitException) as error:
            self.pay.create_order(None, **data)

        self.assertEqual(error.exception.error_info, '商品ID不能为空')
