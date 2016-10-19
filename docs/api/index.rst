wechatkit接口
===============

* 获取 access token

.. code-block:: python

    from wechatkit import WechatAPI
    WechatAPI.get_access_token(appid, appsecret)


* 获取 web access token

.. code-block:: python

    from wechatkit import WechatAPI
    WechatAPI.get_web_access_token(appid, appsecret, code)

* 获取用户信息

.. code-block:: python

    from wechatkit import WechatAPI
    WechatAPI.get_user_info(access_token, openid)

* 获取用户列表

.. code-block:: python

    from wechatkit import WechatAPI
    WechatAPI.get_user_list(access_token, next_openid=None)


* 获取微信服务器列表

.. code-block:: python

    from wechatkit import WechatAPI
    WechatAPI.get_callbackip(access_token)


* sha1 签名  对应微信文档(验证服务器地址的有效性)
.. code-block:: python

    from wechatkit import WechatAPI
    WechatAPI.sha1_encrypt(token, timestamp, nonce)

* 刷新 web access token
.. code-block:: python

    from wechatkit import WechatAPI
    WechatAPI.refresh_web_access_token(appid, refresh_token)
