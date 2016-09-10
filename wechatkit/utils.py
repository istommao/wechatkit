# coding: utf-8
"""Wechatlib utils."""
import requests

from xmltodict import parse

from wechatkit import consts
from wechatkit.exceptions import WechatException


class RequestUtil(object):
    """Wechat api request util."""

    @staticmethod
    def get(url):
        """Get method."""
        try:
            resp = requests.get(url)
            resp.encoding = 'utf-8'
            retdata = resp.json()
        except Exception as error:
            raise WechatException(''.join(error.args))
        else:
            return retdata

    @staticmethod
    def post(url, data, headers=None):
        """Post method."""
        if headers:
            result = requests.post(url, data, headers)
        else:
            result = requests.post(url, data)
        result.encoding = 'utf-8'

        return result.json()

    @staticmethod
    def parse_xml(source):
        """Dict to xml."""
        if not (isinstance(source, dict) and len(source)):
            return None

        xml_template = '<xml>'
        for k in sorted(source):
            value = source.get(k)
            xml_template += ('<{0}><![CDATA[{1}]]></{0}>'.format(k, value))
        xml_template += ('</xml>')

        return xml_template

    @staticmethod
    def post_xml(url, data, cert=None):
        """Post data is xml."""
        result = requests.post(url, data=data.encode(), cert=cert)
        result.encoding = 'utf-8'
        result = dict(parse(result.text).get('xml'))
        return result

    @staticmethod
    def get_retcode_msg(retcode):
        """Get wechat retcode msg."""
        return consts.RETCODE_DICT.get(str(retcode), '未知状态码')


class WechatBasicAPI(object):
    """Wechat basic api."""

    @staticmethod
    def get_access_token(appid, appsecret):
        """Get access token from wechat."""
        url = consts.WECHAT_ACCESS_TOKEN_URL.format(appid, appsecret)

        result = RequestUtil.get(url)

        if result.get('errmsg'):
            raise WechatException(result.get('errmsg'))

        return result

    @staticmethod
    def get_callbackip(access_token):
        """Get wecaht callbackip."""
        url = consts.WECHAT_CALLBACKIP_URL.format(access_token)

        result = RequestUtil.get(url)

        if result.get('errmsg'):
            raise WechatException(result.get('errmsg'))

        return result
