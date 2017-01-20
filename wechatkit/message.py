"""wechatkit message."""
from .utils import RequestUtil


class TemplateMessage(object):
    """Template message."""

    send_url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={}'
    list_url = 'https://api.weixin.qq.com/cgi-bin/template/get_all_private_template?access_token={}'

    @classmethod
    def get_list(cls, access_token):
        """Get template list."""
        url = cls.list_url.format(access_token)
        return RequestUtil.get(url)

    @classmethod
    def send(cls, access_token, payload):
        """Send template message."""
        url = cls.send_url.format(access_token)
        return RequestUtil.post(url, payload)
