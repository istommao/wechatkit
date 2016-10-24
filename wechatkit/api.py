"""Wechatkit api."""
from .basic import WechatBasicAPI
from .user import WechatUserAPI
from .utils import SignUtil
from .payment import WechatPay
from .exceptions import WechatKitException


class WechatAPI(object):
    """WechatAPI."""

    @staticmethod
    def signature(data, key=None):
        """wechat api signature."""
        return SignUtil.sign(data, key=key)

    @staticmethod
    def create_order(appid, mch_id, key, openid=None, **dataset):
        """wechat pay."""
        if not openid:
            raise WechatKitException('参数 openid 不能为空!')

        payment = WechatPay(appid, mch_id, key)

        try:
            payload = {
                'title': dataset['title'],
                'order_uid': dataset['order_uid'],
                'total': dataset['total'],
                'ip': dataset['ip'],
                'trade_type': dataset['trade_type'],
                'notify_url': dataset['notify_url'],
            }
            if 'detail' in dataset:
                payload['detail'] = dataset['detail']

        except KeyError as error:
            raise WechatKitException('参数{}错误!'.format(error))

        result = payment.create_order(openid, **payload)
        return result

    @staticmethod
    def sha1_encrypt(token, timestamp, nonce):
        """Sha1 encrypt."""
        return SignUtil.sha1_encrypt(token, timestamp, nonce)

    @staticmethod
    def _check_exception(result, raise_exception=False):
        if raise_exception and 'errmsg' in result:
            raise WechatKitException(result['errmsg'])

    @staticmethod
    def get_callbackip(access_token, raise_exception=False):
        """Get callbackip."""
        result = WechatBasicAPI.get_callbackip(access_token)
        WechatAPI._check_exception(result, raise_exception=raise_exception)
        return result

    @staticmethod
    def get_web_access_token(appid, appsecret, code, raise_exception=False):
        """Get web access token."""
        result = WechatBasicAPI.get_web_access_token(appid, appsecret, code)
        WechatAPI._check_exception(result, raise_exception=raise_exception)
        return result

    @staticmethod
    def refresh_web_access_token(appid, refresh_token, raise_exception=False):
        """refresh web access token."""
        result = WechatBasicAPI.refresh_web_access_token(appid, refresh_token)
        WechatAPI._check_exception(result, raise_exception=raise_exception)
        return result

    @staticmethod
    def get_access_token(appid, appsecret, raise_exception=False):
        """Get access token."""
        result = WechatBasicAPI.get_access_token(appid, appsecret)
        WechatAPI._check_exception(result, raise_exception=raise_exception)

        return result

    @staticmethod
    def get_user_info(access_token, openid, raise_exception=False):
        """Get user info."""
        result = WechatUserAPI.get_user_info(access_token, openid)
        WechatAPI._check_exception(result, raise_exception=raise_exception)
        return result

    @staticmethod
    def get_web_user_info(access_token, openid, raise_exception=False):
        """Get web user info."""
        result = WechatUserAPI.get_web_user_info(access_token, openid)
        WechatAPI._check_exception(result, raise_exception=raise_exception)
        return result

    @staticmethod
    def get_user_list(access_token, next_openid=None, raise_exception=False):
        """Get user list."""
        result = WechatUserAPI.get_user_list(access_token,
                                             next_openid=next_openid)
        WechatAPI._check_exception(result, raise_exception=raise_exception)

        return result
