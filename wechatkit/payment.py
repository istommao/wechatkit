"""Wechat payment module."""

import uuid

from .exceptions import WechatException
from .utils import SignUtil, RequestUtil


class WechatPay(object):
    """Wechat pay class."""

    WECHAT_ORDER_URI = 'https://api.mch.weixin.qq.com/pay/unifiedorder'
    PAYMENT_JS = 'JSAPI'
    PAYMENT_NATIVE = 'NATIVE'
    PAYMENT_APP = 'APP'

    NOT_NULL_ORDER_DATA = {
        'title': '订单描述不能为空',
        'order_uid': '订单号不能为空',
        'total': '订单总金额不能为空',
        'notify_url': '微信支付回调地址不能为空',
        'ip': '微信支付ip不能为空',
        'trade_type': '交易类型不能为空'
    }

    def __init__(self, appid, mch_id, key):
        self.appid = appid
        self.mch_id = mch_id
        self.key = key

    def create_order(self, openid, **kwargs):
        """Create order with Official Accounts.

        :openid str: order creater
        :kwargs dict: order other data

        :Return dict: create order result from wechat server
        """
        data = kwargs
        data['openid'] = openid

        self._check_create_order(**data)

        order_data = {
            'appid': self.appid,
            'mch_id': self.mch_id,
            'nonce_str': uuid.uuid4().hex,
            'body': kwargs.get('title'),
            'out_trade_no': kwargs.get('order_uid'),
            'total_fee': int(kwargs.get('total') * 100),
            'notify_url': kwargs.get('notify_url'),
            'spbill_create_ip': kwargs.get('ip'),
            'trade_type': kwargs.get('trade_type')
        }
        if 'detail' in kwargs:
            order_data['detail'] = kwargs.get('detail')
        if 'time_expire' in kwargs:
            order_data['time_expire'] = kwargs.get('time_expire')
        if 'time_start' in kwargs:
            order_data['time_start'] = kwargs.get('time_start')
        if 'openid' in kwargs:
            order_data['openid'] = kwargs.get('openid')
        if 'product_id' in kwargs:
            order_data['product_id'] = kwargs.get('product_id')

        return self.send_data(self.WECHAT_ORDER_URI, **order_data)

    def _check_create_order(self, **kwargs):
        """Check create order data with required."""
        error_info = None
        for key in self.NOT_NULL_ORDER_DATA:
            if not kwargs.get(key):
                error_info = self.NOT_NULL_ORDER_DATA.get(key)
                break

        if error_info:
            raise WechatException(error_info)

        trade_type = kwargs.get('trade_type')

        if trade_type == self.PAYMENT_JS:
            if not kwargs.get('openid'):
                raise WechatException('用户标识不能为空')
        elif trade_type == self.PAYMENT_NATIVE:
            if not kwargs.get('product_id'):
                raise WechatException('商品ID不能为空')

    def send_data(self, uri, **order_data):
        """Send data to server."""
        cert = None
        if 'cert' in order_data:
            cert = order_data.pop('cert')

        sign_str = SignUtil.sign(order_data, self.key)
        order_data['sign'] = sign_str

        xml = RequestUtil.generate_xml(order_data)
        resp = RequestUtil.post_xml(uri, xml, cert)

        if resp.get('return_code') != 'SUCCESS':
            raise WechatException(resp.get('return_msg'))

        return resp
