# coding: utf-8
"""Wechatlib utils."""
import hashlib
import requests

from xmltodict import parse

from . import consts
from .exceptions import WechatException


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
    def generate_xml(source):
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
    def upload(url, data, media_path):
        """Upload a media."""
        with open(media_path) as entity:
            result = requests.post(url, data=data, files={'media': entity})
            result.encoding = 'utf-8'
            return result.json()

    @staticmethod
    def get_retcode_msg(retcode):
        """Get wechat retcode msg."""
        return consts.RETCODE_DICT.get(str(retcode), '未知状态码')


class SignUtil(object):
    """Sign util."""

    @classmethod
    def sign(cls, source, key=None):
        """MD5 signature for source.
        :source dict: signature data
        :key str: wechat payment secret key

        :Return str: signature md5 hash value
        """
        result = cls.get_origin_str(source)

        if key:
            signstr = '{}&key={}'.format(result, key)
        else:
            signstr = result

        return hashlib.md5(signstr.encode()).hexdigest().upper()

    @classmethod
    def get_origin_str(cls, source):
        """Get signature origin string.
        :source dict: signature data

        :Return str: signature origin string
        """
        data = dict()
        data.update(source)
        if 'sign' in data:
            data.pop('sign')

        keys = sorted(data)
        result = '&'.join(
            ['{}={}'.format(k, data.get(k)) for k in keys
             if data.get(k) is not None]
        )
        return result
