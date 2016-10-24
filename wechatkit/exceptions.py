"""Wechatkit exception module."""


class WechatKitBaseException(Exception):
    """Wechatkit base Exception."""

    def __init__(self, error_info):
        """Init."""
        super(WechatKitBaseException, self).__init__(error_info)
        self.error_info = error_info


class WechatKitException(WechatKitBaseException):
    """Wechatkit Exception."""


class WechatSignException(WechatKitException):
    """Wechat Sign Exception."""
