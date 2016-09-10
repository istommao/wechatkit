# coding: utf-8
"""Wechatkit tests."""

from unittest import TestCase

from wechatkit import consts
from wechatkit.utils import RequestUtil
from wechatkit.exceptions import WechatException


class RetcodeToMsgTest(TestCase):
    """Retcode to msg test case."""

    def test_get_retcode_msg(self):
        """Test get method with failure."""
        self.assertEqual(RequestUtil.get_retcode_msg(-10), '未知状态码')
        self.assertEqual(RequestUtil.get_retcode_msg(-1),
                         '系统繁忙，此时请开发者稍候再试')
        self.assertEqual(RequestUtil.get_retcode_msg(0), '请求成功')


class RequestUtilTest(TestCase):
    """Request util test case."""

    def test_get_method_failure(self):
        """Test get method with failure."""
        result = RequestUtil.get(consts.WECHAT_ACCESS_TOKEN_URL)
        self.assertEqual(result['errcode'], 40013)

    def test_get_method_exception(self):
        """Test get method with exception."""
        with self.assertRaises(WechatException):
            RequestUtil.get('')
