# coding: utf-8
"""Wechatkit tests."""
from unittest import TestCase

import responses

from wechatkit import consts
from wechatkit.utils import RequestUtil, SignUtil
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

    def test_generate_xml(self):
        """Test dict to xml."""
        data = {
            'server': 'wechat',
            'name': 'xxx'
        }
        result = RequestUtil.generate_xml(data)
        self.assertEqual(
            result,
            ('<xml><name><![CDATA[xxx]]></name><server>'
             '<![CDATA[wechat]]></server></xml>')
        )

    def test_generate_xml_none(self):
        """Test dict is none."""
        result = RequestUtil.generate_xml({})
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
        req_data = RequestUtil.generate_xml(data)
        resp = RequestUtil.post_xml(uri, req_data)
        self.assertEqual(resp['name'], 'wechat')

    @responses.activate
    def test_upload(self):
        """Test upload media."""
        uri = 'http://www.baidu.com'
        responses.add(
            responses.POST, uri, body='''{"type": "image", "media_id": "MEDIA_ID",
                                         "created_at":123456789}''',
            status=200,
            content_type='application/json'
        )

        resp = RequestUtil.upload(uri, {}, './tests/test_requestutil.py')

        self.assertEqual(resp['type'], 'image')


class SignUtilTest(TestCase):
    """SignUtilTest test case."""

    def setUp(self):
        """Init setup."""

    def tearDown(self):
        """Tear down."""

    def test_sign_with_key(self):
        """Test sign with key."""
        data = {
            'name': 'wechat'
        }
        resp = SignUtil.sign(data, 'secret')
        self.assertEqual(resp, '10B479F834276384C96A0F074A1A7AF8')

    def test_sign_no_key(self):
        """Test sign with no key."""
        data = {
            'name': 'wechat'
        }
        resp = SignUtil.sign(data)
        self.assertEqual(resp, 'AF4E19A25809165AF8A6B3F763FA6F03')

    def test_get_origin_str(self):
        """Get sign origin str."""
        data = {'name': 'wechat', 'sign': 'test sign'}

        resp = SignUtil.sign(data)
        self.assertEqual(resp, 'AF4E19A25809165AF8A6B3F763FA6F03')
