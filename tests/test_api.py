"""wechatkit userapi test."""
from decimal import Decimal

from unittest import TestCase
from unittest.mock import patch

from wechatkit.api import WechatAPI

from wechatkit.exceptions import WechatKitException


class WechatAPITest(TestCase):
    """Wechat user api test case."""

    def setUp(self):
        self.appid = 'appid'
        self.mch_id = 'mch_id'
        self.key = 'key'
        self.appsecret = 'appsecret'

    @patch('wechatkit.utils.SignUtil.sign')
    def test_signature(self, mock):
        """Test signature."""
        return_value = 'signature data'
        mock.return_value = return_value

        data, key = 'data', 'key'
        result = WechatAPI.signature(data, key=key)

        self.assertEqual(result, return_value)

    @patch('wechatkit.payment.WechatPay.create_order')
    def test_create_order_failure(self, mock):
        """Test wechat pay create order."""
        mock_data = {
            'prepay_id': 'prepay_id',
            'return_code': 'SUCCESS',
            'return_msg': 'OK',
            'appid': self.appid,
            'mch_id': self.mch_id,
            'sign': '7921E432F65EB8ED0CE9755F0E86D72F',
            'result_code': 'SUCCESS',
            'trade_type': 'JSAPI'
        }
        mock.return_value = mock_data

        dataset = {
            'title': 'title',
            'order_uid': 'order_uid',
            'total': Decimal('10.10'),
            'ip': '127.0.0.1',
            'trade_type': 'JSAPI',
            'notify_url': 'title'
        }
        with self.assertRaises(WechatKitException) as error:
            WechatAPI.create_order(self.appid, self.mch_id, self.key,
                                   openid=None, **dataset)

        self.assertEqual(error.exception.error_info, '参数 openid 不能为空!')

        dataset.pop('title')
        with self.assertRaises(WechatKitException) as error:
            WechatAPI.create_order(self.appid, self.mch_id, self.key,
                                   openid='openid', **dataset)

        self.assertEqual(error.exception.error_info, "参数'title'错误!")

    @patch('wechatkit.payment.WechatPay.create_order')
    def test_create_order(self, mock):
        """Test wechat pay create order."""
        mock_data = {
            'prepay_id': 'prepay_id',
            'return_code': 'SUCCESS',
            'return_msg': 'OK',
            'appid': self.appid,
            'mch_id': self.mch_id,
            'sign': '7921E432F65EB8ED0CE9755F0E86D72F',
            'result_code': 'SUCCESS',
            'trade_type': 'JSAPI'
        }
        mock.return_value = mock_data

        openid = 'openid'
        dataset = {
            'title': 'title',
            'order_uid': 'order_uid',
            'total': Decimal('10.10'),
            'ip': '127.0.0.1',
            'trade_type': 'JSAPI',
            'notify_url': 'title'
        }
        retdata = WechatAPI.create_order(self.appid, self.mch_id, self.key,
                                         openid=openid, **dataset)

        def assert_func(retdata, mock_data):
            """assert func."""
            self.assertEqual(retdata['prepay_id'], mock_data['prepay_id'])
            self.assertEqual(retdata['return_code'], mock_data['return_code'])
            self.assertEqual(retdata['return_msg'], mock_data['return_msg'])
            self.assertEqual(retdata['appid'], mock_data['appid'])
            self.assertEqual(retdata['mch_id'], mock_data['mch_id'])
            self.assertEqual(retdata['sign'], mock_data['sign'])
            self.assertEqual(retdata['result_code'], mock_data['result_code'])
            self.assertEqual(retdata['trade_type'], mock_data['trade_type'])

        assert_func(retdata, mock_data)

        dataset['detail'] = 'detail'
        retdata = WechatAPI.create_order(self.appid, self.mch_id, self.key,
                                         openid=openid, **dataset)
        assert_func(retdata, mock_data)

    def test_sha1_encrypt(self):
        """Test sha1 encrypt."""
        token = 'test_token'
        timestamp = '1461142505'
        nonce = 'sdfklklasdwqieor'

        result = WechatAPI.sha1_encrypt(token, timestamp, nonce)

        self.assertEqual(result, '30eda1491ff3ec8b20489ac38af76dd64ad2a122')

    def test_get_user_info_failure(self):
        """Test get user info failure"""

        access_token, openid = 'access_token', 'openid'
        result = WechatAPI.get_user_info(access_token, openid)
        self.assertIn('errmsg', result)

    def test_get_web_user_info_failure(self):
        """Test get user info failure"""

        access_token, openid = 'access_token', 'openid'
        result = WechatAPI.get_web_user_info(access_token, openid)
        self.assertIn('errmsg', result)

    @patch('wechatkit.utils.RequestUtil.get')
    def test_get_web_user_info(self, mock_data):
        """Test get user info failure"""
        access_token, openid = 'access_token', 'openid'

        payload = {
            'openid': openid,
            'nickname': '昵称',
            'sex': '1',
            'province': 'PROVINCE',
            'city': 'CITY',
            'country':'COUNTRY',
            'headimgurl': 'http://wx.qlogo.cn/mmopen/asf/46',
            'privilege':[
                'PRIVILEGE1'
                'PRIVILEGE2'
            ],
            'unionid': 'o6_bmasdasdsad6_2sgVt7hMZOPfL'
        }

        mock_data.return_value = payload

        result = WechatAPI.get_web_user_info(access_token, openid)

        self.assertEqual(result['openid'], openid)
        self.assertEqual(result['nickname'], payload['nickname'])
        self.assertEqual(result['sex'], payload['sex'])
        self.assertEqual(result['province'], payload['province'])
        self.assertEqual(result['city'], payload['city'])
        self.assertEqual(result['nickname'], payload['nickname'])
        self.assertEqual(result['country'], payload['country'])
        self.assertEqual(result['headimgurl'], payload['headimgurl'])
        self.assertEqual(result['headimgurl'], payload['headimgurl'])
        self.assertEqual(result['privilege'], payload['privilege'])
        self.assertEqual(result['unionid'], payload['unionid'])

    @patch('wechatkit.utils.RequestUtil.get')
    def test_get_user_info(self, mock_data):
        """Test get user basic info."""
        access_token = 'access_token'
        openid = 'o6_bmjrPTlm6_2sgVt7hMZOPfL2M'
        mock_data.return_value = {
            'subscribe': 1,
            'openid': openid,
            'nickname': 'Band',
            'sex': 1,
            'language': 'zh_CN',
            'city': '广州',
            'province': '广东',
            'country': '中国',
            'headimgurl': ('http://wx.qlogo.cn/mmopen/g3MonUZtNHkdmzicIlibx6ia'
                           'FqAc56vxLSUfpb6n5WKSYVY0ChQKkiaJSgQ1dZuTOgvLLrhJbE'
                           'RQQ4eMsv84eavHiaiceqxibJxCfHe/0'),
            'subscribe_time': 1382694957,
            'unionid': 'o6_bmasdasdsad6_2sgVt7hMZOPfL',
            'remark': '',
            'groupid': 0
        }
        resp = WechatAPI.get_user_info(access_token, openid)

        self.assertEqual(resp.get('openid'), openid)

    @patch('wechatkit.utils.RequestUtil.get')
    def test_get_user_list(self, mock_data):
        """Test get user list."""
        access_token = 'access_token'
        mock_data.return_value = {
            'user_info_list': [
                {
                    'subscribe': 1,
                    'openid': 'otvxTs4dckWG7imySrJd6jSi0CWE',
                    'nickname': 'iWithery',
                    'sex': 1,
                    'language': 'zh_CN',
                    'city': 'Jieyang',
                    'province': 'Guangdong',
                    'country': 'China',
                    'headimgurl': ('http://wx.qlogo.cn/mmopen/xbIQx1GRqdvyqkMM'
                                   'hEaGOX802l1CyqMJNgUzKP8MeAeHFicRDSnZH7FY4X'
                                   'B7p8XHXIf6uJA2SCunTPic'
                                   'GKezDC4saKISzRj3nz/0'),
                    'subscribe_time': 1434093047,
                    'unionid': 'oR5GjjgEhCMJFyzaVZdrxZ2zRRF4',
                    'remark': '',
                    'groupid': 0
                },
                {
                    'subscribe': 0,
                    'openid': 'otvxTs_JZ6SEiP0imdhpi50fuSZg',
                    'unionid': 'oR5GjjjrbqBZbrnPwwmSxFukE41U'
                }
            ]
        }
        resp = WechatAPI.get_user_list(access_token)

        self.assertEqual(len(resp['user_info_list']), 2)

    @patch('wechatkit.utils.RequestUtil.get')
    def test_get_user_list_next_openid(self, mock_data):
        """Test get user list with next openid."""
        access_token = 'access_token'
        openid = 'openid'
        mock_data.return_value = {
            'user_info_list': [
                {
                    'subscribe': 1,
                    'openid': 'otvxTs4dckWG7imySrJd6jSi0CWE',
                    'nickname': 'iWithery',
                    'sex': 1,
                    'language': 'zh_CN',
                    'city': 'Jieyang',
                    'province': 'Guangdong',
                    'country': 'China',
                    'headimgurl': ('http://wx.qlogo.cn/mmopen/xbIQx1GRqdvyqkMM'
                                   'hEaGOX802l1CyqMJNgUzKP8MeAeHFicRDSnZH7FY4X'
                                   'B7p8XHXIf6uJA2SCunTPic'
                                   'GKezDC4saKISzRj3nz/0'),
                    'subscribe_time': 1434093047,
                    'unionid': 'oR5GjjgEhCMJFyzaVZdrxZ2zRRF4',
                    'remark': '',
                    'groupid': 0
                },
                {
                    'subscribe': 0,
                    'openid': 'otvxTs_JZ6SEiP0imdhpi50fuSZg',
                    'unionid': 'oR5GjjjrbqBZbrnPwwmSxFukE41U'
                }
            ]
        }
        resp = WechatAPI.get_user_list(access_token, next_openid=openid)

        self.assertEqual(len(resp['user_info_list']), 2)

    def test_get_user_list_failure(self):
        """Test get user list failure"""

        access_token = 'access_token'
        result = WechatAPI.get_user_list(access_token)
        self.assertIn('errmsg', result)

    @patch('wechatkit.utils.RequestUtil.get')
    def test_get_access_token_success(self, mock_data):
        """Test get access token."""
        mock_data.return_value = {
            'access_token': 'access_token',
            'expires_in': 7200
        }
        resp = WechatAPI.get_access_token(self.appid, self.appsecret)

        self.assertEqual(resp.get('access_token'), 'access_token')

    def test_get_access_token_failure(self):
        """Test."""
        result = WechatAPI.get_access_token(self.appid, self.appsecret)
        self.assertIn('errmsg', result)

    @patch('wechatkit.utils.RequestUtil.get')
    def test_get_callbackip(self, mock_data):
        """Test get callback ip."""
        access_token = 'access_token'
        mock_data.return_value = {
            'ip_list': ['127.0.0.1', '127.0.0.1']
        }
        resp = WechatAPI.get_callbackip(access_token)

        self.assertEqual(len(resp['ip_list']), 2)

    def test_get_callbackip_failure(self):
        """Test."""
        access_token = 'access_token'
        result = WechatAPI.get_callbackip(access_token)
        self.assertIn('errmsg', result)

    @patch('wechatkit.utils.RequestUtil.get')
    def test_refresh_web_token(self, mock_data):
        """Test get web access token success."""
        refresh_token = 'refresh_token'
        mock_data.return_value = {
            "access_token": "ACCESS_TOKEN",
            "expires_in": 7200,
            "refresh_token": "REFRESH_TOKEN",
            "openid": "OPENID",
            "scope": "SCOPE"
        }
        result = WechatAPI.refresh_web_access_token(
            self.appid, refresh_token
        )
        self.assertEqual(result.get('access_token'), 'ACCESS_TOKEN')

    @patch('wechatkit.utils.RequestUtil.get')
    def test_get_web_token(self, mock_data):
        """Test get web access token success."""
        mock_data.return_value = {
            "access_token": "ACCESS_TOKEN",
            "expires_in": 7200,
            "refresh_token": "REFRESH_TOKEN",
            "openid": "OPENID",
            "scope": "SCOPE"
        }
        result = WechatAPI.get_web_access_token(
            self.appid, self.appsecret, 'code')

        self.assertEqual(result.get('access_token'), 'ACCESS_TOKEN')

    @patch('wechatkit.utils.RequestUtil.get')
    def test_get_token_failure(self, mock_data):
        """Test get web access token failure."""
        mock_data.return_value = {
            "errcode": 40029,
            "errmsg": "invalid code"
        }
        result = WechatAPI.get_web_access_token(self.appid, self.appsecret,
                                                'code')
        self.assertIn('errmsg', result)

    @patch('wechatkit.utils.RequestUtil.get')
    def test_get_token_raise_exception(self, mock_data):
        """Test get web access token failure."""
        mock_data.return_value = {
            "errcode": 40029,
            "errmsg": "invalid code"
        }

        with self.assertRaises(WechatKitException) as error:
            WechatAPI.get_web_access_token(self.appid, self.appsecret, 'code',
                                           raise_exception=True)

        self.assertEqual(error.exception.error_info, '不合法的oauth_code')
