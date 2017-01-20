# -*- coding: utf-8 -*-
"""wechatkit test message."""

from unittest import TestCase
from unittest.mock import patch

from wechatkit import TemplateMessage


class TemplateMessageTest(TestCase):
    """Template message test."""

    @patch('wechatkit.utils.RequestUtil.get')
    def test_get_list(self, mock):
        """Test send."""
        retval = {
            "errcode": 0,
            "errmsg": "ok",
            "msgid": 200228332
        }
        mock.return_value = retval

        retdata = TemplateMessage.get_list('access_token')

        self.assertEqual(retdata, retval)

    @patch('wechatkit.utils.RequestUtil.post')
    def test_send(self, mock):
        """Test send."""
        retval = {
            "errcode": 0,
            "errmsg": "ok",
            "template_id": "Doclyl5uP7Aciu-qZ7mJNPtWkbkYnWBWVja26EGbNyk"
        }
        mock.return_value = retval

        payload = {
            "touser": "OPENID",
            "template_id": "ngqIpbwh8bUfcSsECmogfXcV14J0tQlEpBO27izEYtY",
            "url": "http://weixin.qq.com/download",
            "data": {
                "first": {
                    "value": "data",
                    "color": "#173177"
                },
                "keynote1": {
                    "value": "data",
                    "color": "#173177"
                },
                "keynote2": {
                    "value": "39.8元",
                    "color": "#173177"
                },
                "keynote3": {
                    "value": "2014年9月22日",
                    "color": "#173177"
                },
                "remark": {
                    "value": "data",
                    "color": "#173177"
                }
            }
        }
        retdata = TemplateMessage.send('access_token', payload)

        self.assertEqual(retdata, retval)
