## 网页授权 获取web令牌

```python
from wechatkit import WechatAPI

WechatAPI.get_web_access_token(appid, appsecret, code)
```

- 返回结果

```json
{
    "access_token": "ACCESS_TOKEN",
    "expires_in": 7200,
    "refresh_token": "REFRESH_TOKEN",
    "openid": "OPENID",
    "scope": "SCOPE"
}
```

## 网页授权 获取用户信息

```python
from wechatkit import WechatAPI

WechatAPI.get_web_user_info(access_token, openid)
```


- 返回结果

```json
{
    "openid": "OPENID",
    "nickname": "NICKNAME",
    "sex": "1",
    "province": "PROVINCE",
    "city": "CITY",
    "country": "COUNTRY",
    "headimgurl": "http://wx.qlogo.cn/mmopen/g3MonUZtNHkdmzicIlibx6iaFqAc56vxLSUfpb6n5WKSYVY0ChQKkiaJSgQ1dZuTOgvLLrhJbERQQ4eMsv84eavHiaiceqxibJxCfHe/46",
    "privilege": [
        "PRIVILEGE1",
        "PRIVILEGE2"
    ],
    "unionid": "o6_bmasdasdsad6_2sgVt7hMZOPfL"
}
```

## 网页授权 获取jsapi ticket

```python
from wechatkit import WechatAPI

WechatAPI.get_jsapi_ticket(web_token)
```


- 返回结果

```json
{
    "errcode": 0,
    "errmsg": "ok",
    "ticket": "bxLdikRXVbTPdHSM05e5u5sUoXNKdvsdshFKA",
    "expires_in": 7200
}
```