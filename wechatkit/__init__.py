"""wechatkit init."""

from .api import WechatAPI
from .message import TemplateMessage

__all__ = [
    'WechatAPI',
    'TemplateMessage'
]
