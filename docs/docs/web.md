## 获取 web access token

```python
from wechatkit import WechatAPI

WechatAPI.get_web_access_token(appid, appsecret, code)
```

## 网页授权 获取 用户信息

```python
from wechatkit import WechatAPI

WechatAPI.get_web_user_info(access_token, openid)
```