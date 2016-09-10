# coding: utf-8
"""Wechatlib utils."""
import requests

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
    def get_retcode_msg(retcode):
        """Get wechat retcode msg."""
        return consts.RETCODE_DICT.get(str(retcode), '未知状态码')
