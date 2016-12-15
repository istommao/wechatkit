
# wechatkit
> wechatkit is a common wechat api component.

## Feature Support
- wechat payment

## Installation

To install wechatkit, simply:

```
pip install wechatkit
```

## Usage

```python
from wechatkit import WechatAPI

WechatAPI.get_access_token(appid, appsecret)
WechatAPI.get_web_access_token(appid, appsecret)

WechatAPI.get_callbackip(access_token)

WechatAPI.get_user_info(access_token, openid)
WechatAPI.get_user_list(access_token, openid)

WechatAPI.get_jsapi_ticket(web_token)
```

## ChangeLog

[changelog](https://github.com/istommao/wechatkit/blob/master/changelog.md)

## License

MIT. See [LICENSE](https://github.com/istommao/wechatkit/blob/master/LICENSE) for more details.
