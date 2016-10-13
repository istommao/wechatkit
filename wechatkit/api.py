"""Wechatkit api."""
from .basic import WechatBasicAPI
from .user import WechatUserAPI


class WechatAPI(object):
    """WechatAPI."""

    @staticmethod
    def get_callbackip(access_token):
        """Get callbackip."""
        return WechatBasicAPI.get_callbackip(access_token)

    @staticmethod
    def get_web_access_token(appid, appsecret, code):
        """Get web access token."""
        return WechatBasicAPI.get_web_access_token(appid, appsecret, code)

    @staticmethod
    def get_access_token(appid, appsecret):
        """Get access token."""
        return WechatBasicAPI.get_access_token(appid, appsecret)

    @staticmethod
    def get_user_info(access_token, openid):
        """Get user info."""
        return WechatUserAPI.get_user_basic_info(access_token, openid)

    @staticmethod
    def get_user_list(access_token, next_openid=None):
        """Get user list."""
        return WechatUserAPI.get_user_list(access_token,
                                           next_openid=next_openid)
