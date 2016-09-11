"""wechatkit basic"""

from wechatkit import consts
from wechatkit.utils import RequestUtil
from wechatkit.exceptions import WechatException


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
