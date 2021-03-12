"""实名认证结果查询接口"""

import time

import requests

from util import get_sign

URL = "https://wlc.nppa.gov.cn/test/authentication/query/%s"


def test_case04(the_cfg, test_code):
    _url = URL % test_code

    headers = {
        "appId": the_cfg.app_id,
        "bizId": the_cfg.biz_id,
        "timestamps": str("%.3f" % time.time()).replace(".", ""),
    }
    data = {
        "ai": "100000000000000001"
    }
    headers.update(data)
    headers.update({
        "Content-Type": "application/json; charset=utf-8",
        "sign": get_sign(headers, '', the_cfg.secret_key)
    })
    headers.pop('ai')
    res = requests.get(_url, params=data, headers=headers)
    print(res.content)


def test_case05(the_cfg, test_code):
    _url = URL % test_code

    headers = {
        "appId": the_cfg.app_id,
        "bizId": the_cfg.biz_id,
        "timestamps": str("%.3f" % time.time()).replace(".", ""),
    }
    data = {
        "ai": "200000000000000001"
    }
    headers.update(data)
    headers.update({
        "Content-Type": "application/json; charset=utf-8",
        "sign": get_sign(headers, '', the_cfg.secret_key)
    })
    headers.pop('ai')
    res = requests.get(_url, params=data, headers=headers)
    print(res.content)


def test_case06(the_cfg, test_code):
    _url = URL % test_code

    headers = {
        "appId": the_cfg.app_id,
        "bizId": the_cfg.biz_id,
        "timestamps": str("%.3f" % time.time()).replace(".", ""),
    }
    data = {
        "ai": "300000000000000001"
    }
    headers.update(data)
    headers.update({
        "Content-Type": "application/json; charset=utf-8",
        "sign": get_sign(headers, '', the_cfg.secret_key)
    })
    headers.pop('ai')
    res = requests.get(_url, params=data, headers=headers)
    print(res.content)
