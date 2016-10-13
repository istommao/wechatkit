# coding: utf-8
"""Wechatkit tests."""

from unittest import TestCase
from unittest.mock import patch

from wechatkit.basic import WechatBasicAPI
from wechatkit.exceptions import WechatException


class WechatBasicAPITest(TestCase):
    """Wechat basic api test case."""

    def setUp(self):
        self.appid = 'appid'
        self.appsecret = 'appsecret'

    @patch('wechatkit.utils.RequestUtil.get')
    def test_get_access_token_success(self, mock_data):
        """Test get access token."""
        mock_data.return_value = {
            'access_token': 'access_token',
            'expires_in': 7200
        }
        resp = WechatBasicAPI.get_access_token(self.appid, self.appsecret)

        self.assertEqual(resp.get('access_token'), 'access_token')

    def test_get_access_token_failure(self):
        with self.assertRaises(WechatException):
            WechatBasicAPI.get_access_token(self.appid, self.appsecret)

    @patch('wechatkit.utils.RequestUtil.get')
    def test_get_callbackip(self, mock_data):
        """Test get callback ip."""
        access_token = 'access_token'
        mock_data.return_value = {
            'ip_list': ['127.0.0.1', '127.0.0.1']
        }
        resp = WechatBasicAPI.get_callbackip(access_token)

        self.assertEqual(len(resp['ip_list']), 2)

    def test_get_callbackip_failure(self):
        with self.assertRaises(WechatException):
            access_token = 'access_token'
            WechatBasicAPI.get_callbackip(access_token)

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
        result = WechatBasicAPI.get_web_access_token(
            self.appid, self.appsecret, 'code')

        self.assertEqual(result.get('access_token'), 'ACCESS_TOKEN')

    @patch('wechatkit.utils.RequestUtil.get')
    def test_get_token_failure(self, mock_data):
        """Test get web access token failure."""
        mock_data.return_value = {
            "errcode": 40029,
            "errmsg": "invalid code"
        }
        with self.assertRaises(WechatException):
            WechatBasicAPI.get_web_access_token(self.appid, self.appsecret,
                                                'code')
