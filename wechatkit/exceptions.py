"""Wechatkit exception module."""


class WechatkitBaseException(Exception):
    """Wechatkit Exception."""

    def __init__(self, error_info):
        """Init."""
        super(WechatkitBaseException, self).__init__(error_info)
        self.error_info = error_info


class WechatException(WechatkitBaseException):
    """Wechatkit Exception."""


class WechatSignException(WechatException):
    """Wechat Sign Exception."""
