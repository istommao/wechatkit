## 获取用户信息

```python
from wechatkit import WechatAPI

WechatAPI.get_user_info(access_token, openid)
```

- 返回结果

```json
{
    "subscribe": 1,
    "openid": "o6_bmjrPTlm6_2sgVt7hMZOPfL2M",
    "nickname": "Band",
    "sex": 1,
    "language": "zh_CN",
    "city": "广州",
    "province": "广东",
    "country": "中国",
    "headimgurl": "http://wx.qlogo.cn/mmopen/g3MonUZtNHkdmzicIlibx6iaFqAc56vxLSUfpb6n5WKSYVY0ChQKkiaJSgQ1dZuTOgvLLrhJbERQQ4eMsv84eavHiaiceqxibJxCfHe/0",
    "subscribe_time": 1382694957,
    "unionid": "o6_bmasdasdsad6_2sgVt7hMZOPfL",
    "remark": "",
    "groupid": 0,
    "tagid_list": [
        128,
        2
    ]
}
```


## 获取用户列表

```python
from wechatkit import WechatAPI

WechatAPI.get_user_list(access_token, next_openid=None)
```

- 返回结果

```json
{
    "user_list": [
        {
            "openid": "otvxTs4dckWG7imySrJd6jSi0CWE",
            "lang": "zh-CN"
        },
        {
            "openid": "otvxTs_JZ6SEiP0imdhpi50fuSZg",
            "lang": "zh-CN"
        }
    ]
}
```