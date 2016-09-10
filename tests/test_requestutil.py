# coding: utf-8
"""Wechatkit tests."""
from unittest import TestCase

import responses

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

    def test_post_method(self):
        """Test post method."""
        result = RequestUtil.post(consts.WECHAT_ACCESS_TOKEN_URL, {})
        self.assertEqual(result['errcode'], 40013)

    def test_post_method_with_header(self):
        """Test post method."""
        result = RequestUtil.post(
            consts.WECHAT_ACCESS_TOKEN_URL, {},
            headers={'content_type': 'application/json'}
        )
        self.assertEqual(result['errcode'], 40013)

    def test_parse_xml(self):
        """Test dict to xml."""
        data = {
            'server': 'wechat',
            'name': 'xxx'
        }
        result = RequestUtil.parse_xml(data)
        self.assertEqual(
            result,
            ('<xml><name><![CDATA[xxx]]></name><server>'
             '<![CDATA[wechat]]></server></xml>')
        )

    def test_parse_xml_none(self):
        """Test dict is none."""
        result = RequestUtil.parse_xml({})
        self.assertIsNone(result)

    @responses.activate
    def test_post_xml(self):
        """Test post xml data."""
        uri = 'http://www.baidu.com'
        responses.add(
            responses.POST, uri, body='''<xml><name>wechat</name></xml>''',
            status=200,
            content_type='application/xml'
        )
        data = {
            'server': 'wechat',
            'name': 'xxx'
        }
        req_data = RequestUtil.parse_xml(data)
        resp = RequestUtil.post_xml(uri, req_data)
        self.assertEqual(resp['name'], 'wechat')
