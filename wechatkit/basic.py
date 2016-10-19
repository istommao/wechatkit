"""wechatkit basic"""

from . import consts
from .utils import RequestUtil


class WechatBasicAPI(object):
    """Wechat basic api."""

    @staticmethod
    def get_access_token(appid, secret):
        """Get access token from wechat."""
        url = consts.WECHAT_ACCESS_TOKEN_URL.format(appid=appid, secret=secret)

        return RequestUtil.get_result(url)

    @staticmethod
    def refresh_web_access_token(appid, refresh_token):
        """Refresh web access token."""
        url = consts.WECHAT_REFRESH_TOKEN_URL.format(
            appid=appid, refresh_token=refresh_token)
        return RequestUtil.get_result(url)

    @staticmethod
    def get_callbackip(access_token):
        """Get wecaht callbackip."""
        url = consts.WECHAT_CALLBACKIP_URL.format(access_token=access_token)

        return RequestUtil.get_result(url)


    @staticmethod
    def get_web_access_token(appid, appsecret, code):
        """Get web access toekn differ from base access token."""
        urlfmt = '{}appid={}&secret={}&code={}&grant_type=authorization_code'
        url = urlfmt.format(consts.WECHAT_WEB_AUTH_ACCESS_TOKEN_URI,
                            appid, appsecret, code)

        return RequestUtil.get_result(url)
