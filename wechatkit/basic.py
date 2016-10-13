"""wechatkit basic"""

from . import consts
from .utils import RequestUtil
from .exceptions import WechatException


class WechatBasicAPI(object):
    """Wechat basic api."""

    @staticmethod
    def get_access_token(appid, appsecret):
        """Get access token from wechat."""
        url = consts.WECHAT_ACCESS_TOKEN_URL.format(appid, appsecret)

        result = RequestUtil.get(url)

        if result.get('errmsg'):
            errmsg = RequestUtil.get_retcode_msg(result.get('errcode'))
            raise WechatException(errmsg)

        return result

    @staticmethod
    def get_callbackip(access_token):
        """Get wecaht callbackip."""
        url = consts.WECHAT_CALLBACKIP_URL.format(access_token)

        result = RequestUtil.get(url)

        if result.get('errmsg'):
            errmsg = RequestUtil.get_retcode_msg(result.get('errcode'))
            raise WechatException(errmsg)

        return result

    @staticmethod
    def get_web_access_token(appid, appsecret, code):
        """Get web access toekn differ from base access token."""
        urlfmt = '{}appid={}&secret={}&code={}&grant_type=authorization_code'
        url = urlfmt.format(consts.WECHAT_WEB_AUTH_ACCESS_TOKEN_URI,
                            appid, appsecret, code)
        result = RequestUtil.get(url)

        if result.get('errmsg'):
            errmsg = RequestUtil.get_retcode_msg(result.get('errcode'))
            raise WechatException(errmsg)

        return result
