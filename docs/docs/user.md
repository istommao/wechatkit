## 获取用户信息

```python
from wechatkit import WechatAPI

WechatAPI.get_user_info(access_token, openid)
```

## 获取用户列表

```python
from wechatkit import WechatAPI

WechatAPI.get_user_list(access_token, next_openid=None)
```