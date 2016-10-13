"""wechatkit user"""
from wechatkit import consts
from wechatkit.utils import RequestUtil
from wechatkit.exceptions import WechatException


class WechatUserAPI(object):
    """Wechat user api."""

    @staticmethod
    def get_user_basic_info(access_token, openid):
        """Get user basic info."""
        url = consts.WECHAT_USER_INFO_URL.format(access_token, openid, 'zh_CN')

        result = RequestUtil.get(url)

        if result.get('errmsg'):
            errmsg = RequestUtil.get_retcode_msg(result.get('errcode'))
            raise WechatException(errmsg)

        return result

    @staticmethod
    def get_user_list(access_token, next_openid=None):
        """Get uesr list."""
        url = consts.WECHAT_USER_LIST_URL.format(access_token)

        if next_openid:
            url = '{}&next_openid={}'.format(url, next_openid)

        result = RequestUtil.get(url)

        if result.get('errmsg'):
            errmsg = RequestUtil.get_retcode_msg(result.get('errcode'))
            raise WechatException(errmsg)

        return result
