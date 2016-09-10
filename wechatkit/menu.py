"""Wechat custom Menu module."""

from wechatkit.utils import RequestUtil


class MenuUtil(object):
    """Wechat custome menu util class."""

    WECHAT_MENU_QUERY_URL = ('https://api.weixin.qq.com/cgi-bin/menu/'
                             'get?access_token={}')
    WECHAT_MENU_CREATE_URL = ('https://api.weixin.qq.com/cgi-bin/menu/'
                              'create?access_token={}')
    WECHAT_MENU_DELETE_URL = ('https://api.weixin.qq.com/cgi-bin/menu/'
                              'delete?access_token={}')

    @classmethod
    def query(cls, token):
        """Query custom menu with already exists.
        :token str: wechat base access token

        :Return dict:
        """
        resp = RequestUtil.get(cls.WECHAT_MENU_QUERY_URL.format(token))
        return resp

    @classmethod
    def create(cls, data, token):
        """Create custom menu with json data.
        :data dict: Custom Menu data
        :token str: wechat base access token
        :Return dict:
        """
        resp = RequestUtil.post(
            cls.WECHAT_MENU_CREATE_URL.format(token),
            data=data
        )
        return resp

    @classmethod
    def delete(cls, token):
        """Delete custom menu.
        :token str: wechat base access token
        :Return dict:
        """
        resp = RequestUtil.get(cls.WECHAT_MENU_DELETE_URL.format(token))

        return resp
