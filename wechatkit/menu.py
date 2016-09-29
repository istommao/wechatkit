"""Wechat custom Menu module."""

from wechatkit.utils import RequestUtil
from wechatkit.exceptions import WechatException


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


class AbstractButton(object):
    """ Abstract Button for wechat custom menu. """
    ab_type = None
    name = None

    def __init__(self, **kwargs):
        if kwargs.get('data', None):
            self.parse(kwargs['data'])
        else:
            self.parse(kwargs)

    def json(self):
        """ convert button to json. """
        result = self.__dict__.copy()

        if 'ab_type' in result:
            temp = result.pop('ab_type')
            result['type'] = temp

        if 'buttons' in result:
            result.pop('buttons')

        if hasattr(self, 'buttons'):
            result['sub_button'] = []
            for button in self.buttons:
                result['sub_button'].append(button.json())

        return result

    def parse(self, data):
        """ parse json to button. """
        for key, value in data.items():
            if key == 'type':
                key = 'ab_type'

            if hasattr(self, key):
                if not value:
                    raise WechatException('Not empty for `{}`'.format(key))
                setattr(self, key, value)

            if key == SubButton.TYPE and hasattr(self, 'buttons'):
                for item in value:
                    button = ButtonFactory.convert(item)
                    self.buttons.append(button)


class MenuButton(AbstractButton):
    """ Base Menu Button. """

    buttons = None

    def __init__(self):
        self.buttons = []
        super().__init__()

    def json(self):
        result = {'button': []}

        for button in self.buttons:
            result['button'].append(button.json())

        return result

    def parse(self, data):
        """
        :data dict: button json data.
        """
        buttons = data.get('button', [])
        for button in buttons:
            self.buttons.append(ButtonFactory.convert(button))

    def add(self, button):
        """ Add sub button to menu button.
        :button AbstractButton: Sub button.
        """
        if len(self.buttons) >= 3:
            raise WechatException('Level menu must not more than 3')

        self.buttons.append(button)

    def remove(self, index=0):
        """ Remove sub button from menu button.
        :index int: sub button index.
        """
        if index >= len(self.buttons):
            raise WechatException('Sub button not exists')

        return self.buttons.pop(index)


class SubButton(AbstractButton):
    """ Sub button. """
    TYPE = 'sub_button'
    buttons = None

    def __init__(self, name=None, data=None):
        self.buttons = []
        super().__init__(name=name, data=data)

    def add(self, button):
        """ Add sub button to menu button.
        :button AbstractButton: Sub button.
        """
        if len(self.buttons) >= 5:
            raise WechatException('Secondary submenu must not more than 5')

        self.buttons.append(button)

    def remove(self, index=0):
        """ Remove sub button from menu button.
        :index int: sub button index.
        """
        if index >= len(self.buttons):
            raise WechatException('Sub button not exists')

        return self.buttons.pop(index)

class ClickButton(AbstractButton):
    """ Click button. """
    TYPE = 'click'
    key = None

    def __init__(self, name=None, key=None, type_name=TYPE, data=None):
        super().__init__(name=name, type=type_name, key=key, data=data)


class ViewButton(AbstractButton):
    """ View button. """
    TYPE = 'view'
    url = None

    def __init__(self, name=None, url=None, type_name=TYPE, data=None):
        super().__init__(name=name, type=type_name, url=url, data=data)


class ScanButton(AbstractButton):
    """ Scan button. """
    SCAN_PUSH = 'scancode_push'
    SCAN_WAIT = 'scancode_waitmsg'
    key = ''

    def __init__(self, name=None, key=None, type_name=SCAN_PUSH, data=None):
        super().__init__(name=name, type=type_name, key=key, data=data)


class PhotoButton(AbstractButton):
    """ Photo button. """
    PIC_SYS_PHOTO = 'pic_sysphoto'
    PIC_SYS_OPTION = 'pic_photo_or_album'
    PIC_WEIXIN = 'pic_weixin'
    key = ''

    def __init__(self, name=None, key=None, type_name=PIC_SYS_OPTION, data=None):
        super().__init__(name=name, type=type_name, key=key, data=data)


class LocationButton(AbstractButton):
    """ Location button. """
    TYPE = 'location_select'
    key = ''

    def __init__(self, name=None, key=None, type_name=TYPE, data=None):
        super().__init__(name=name, type=type_name, key=key, data=data)


class MediaButton(AbstractButton):
    """ Media button. """
    MEDIA = 'media_id'
    LIMITED = 'view_limited'
    media_id = ''

    def __init__(self, name=None, media_id=None, type_name=MEDIA, data=None):
        super().__init__(name=name, type=type_name, media_id=media_id, data=data)


class ButtonFactory(object):
    """ Button factory. """

    types = {
        'click': ClickButton,
        'view': ViewButton,
        'scancode_push': ScanButton,
        'scancode_waitmsg': ScanButton,
        'pic_sysphoto': PhotoButton,
        'pic_photo_or_album': PhotoButton,
        'pic_weixin': PhotoButton,
        'location_select': LocationButton,
        'media_id': MediaButton,
        'view_limited': MediaButton,
    }

    @classmethod
    def convert(cls, data):
        """ Convert json to object.
        :data dict: button json

        :return AbstractButton: button object
        """
        _type = data.get('type', SubButton)
        if isinstance(_type, str):
            class_name = cls.types[_type]
        else:
            class_name = _type

        return class_name(data=data)
