[![Build Status](https://travis-ci.org/istommao/wechatkit.svg?branch=master)](https://travis-ci.org/istommao/wechatkit)
[![codecov](https://codecov.io/gh/istommao/wechatkit/branch/master/graph/badge.svg)](https://codecov.io/gh/istommao/wechatkit)
[![PyPI](https://img.shields.io/pypi/v/wechatkit.svg)](https://pypi.python.org/pypi/wechatkit)

# Introduction
wechatkit is a common wechat api component.

# Document

[wechatkit document](http://wechatkit.codingcat.top/)

# Feature Support

- Wechat payment
- User api
- OAuth validation

# Installation

To install wechatkit, simply:

> pip install wechatkit

# Usage

```python
from wechatkit import WechatAPI

WechatAPI.get_access_token(appid, appsecret)
WechatAPI.get_web_access_token(appid, appsecret)

WechatAPI.get_callbackip(access_token)

WechatAPI.get_user_info(access_token, openid)
WechatAPI.get_user_list(access_token, openid)

WechatAPI.get_jsapi_ticket(web_token)
```

# ChangeLog

[changelog](changelog.md)

# License

MIT. See [LICENSE](https://github.com/istommao/wechatkit/blob/master/LICENSE) for more details.

