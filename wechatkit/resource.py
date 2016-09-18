"""Resource manage module."""
import os

from wechatkit.utils import RequestUtil


class ResourceAPI(object):
    """Resource wechat api."""

    ADD_TEMP_URI = ('https://api.weixin.qq.com/cgi-bin/media/'
                    'upload?access_token={}&type={}')

    @classmethod
    def upload(cls, path, token, rtype, upload_type='temp'):
        """Upload resource.
        :path str: Resource local path
        :token str: Wechat access token
        :rtype str: Resource type such as image, voice ...
        :upload_type: Upload type, Now support temp and forever
        """
        if not os.path.exists(path):
            return False

        method = getattr(cls, '_upload_{}'.format(upload_type), None)

        if method:
            return method(path, token, rtype)

        return False

    @classmethod
    def _upload_temp(cls, path, token, rtype):
        """Upload temp media to wechat server.
        :path str: Upload entity local path
        :token str: Wechat access token
        :rtype str: Upload entity type

        :Return dict:
        """
        uri = cls.ADD_TEMP_URI.format(token, rtype)

        resp = RequestUtil.upload(uri, {}, path)

        return resp
