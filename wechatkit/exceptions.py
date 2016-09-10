"""Wechatkit exception module."""


class WechatException(Exception):
    """Wechatkit Exception."""

    def __init__(self, error_info):
        """Init."""
        super(WechatException, self).__init__(error_info)
        self.error_info = error_info
