"""wechatkit userapi test."""
from unittest import TestCase
from unittest.mock import patch

from wechatkit.user import WechatUserAPI
from wechatkit.exceptions import WechatException


class WechatUserAPITest(TestCase):
    """Wechat user api test case."""

    def setUp(self):
        self.appid = 'appid'
        self.appsecret = 'appsecret'

    def test_get_user_info_failure(self):
        """Test get user info failure"""

        with self.assertRaises(WechatException):
            access_token, openid = 'access_token', 'openid'
            WechatUserAPI.get_user_basic_info(access_token, openid)

    @patch('wechatkit.utils.RequestUtil.get')
    def test_get_user_basic_info(self, mock_data):
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
        resp = WechatUserAPI.get_user_basic_info(access_token, openid)

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
        resp = WechatUserAPI.get_user_list(access_token)

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
        resp = WechatUserAPI.get_user_list(access_token, next_openid=openid)

        self.assertEqual(len(resp['user_info_list']), 2)

    def test_get_user_list_failure(self):
        """Test get user list failure"""

        with self.assertRaises(WechatException):
            access_token = 'access_token'
            WechatUserAPI.get_user_list(access_token)
