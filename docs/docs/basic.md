## 获取access_token

```python
from wechatkit import WechatAPI

WechatAPI.get_access_token(appid, appsecret)
```

- 返回结果

```json
{
    "access_token": "ACCESS_TOKEN",
    "expires_in": 7200
}
```

## 获取微信服务ip

```python
from wechatkit import WechatAPI

WechatAPI.get_callbackip(access_token)
```

- 返回结果

```json
{
    "ip_list": [
        "127.0.0.1",
        "127.0.0.2",
        "101.226.103.0/25"
    ]
}
```