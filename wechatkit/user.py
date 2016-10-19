"""wechatkit user"""
from . import consts
from .utils import RequestUtil


class WechatUserAPI(object):
    """Wechat user api."""

    @staticmethod
    def get_web_user_info(access_token, openid):
        """Get web user info."""
        url = consts.WECHAT_WEB_USER_INFO_URL.format(
            access_token=access_token, openid=openid, lang='zh_CN')

        return RequestUtil.get_result(url)

    @staticmethod
    def get_user_info(access_token, openid):
        """Get user basic info."""
        url = consts.WECHAT_USER_INFO_URL.format(access_token=access_token,
                                                 openid=openid, lang='zh_CN')

        return RequestUtil.get_result(url)

    @staticmethod
    def get_user_list(access_token, next_openid=None):
        """Get uesr list."""
        url = consts.WECHAT_USER_LIST_URL.format(access_token=access_token)

        if next_openid:
            url = '{}&next_openid={}'.format(url, next_openid)

        return RequestUtil.get_result(url)
