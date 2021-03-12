"""游戏用户行为数据上报接口"""

import json
import time

import requests

from util import get_sign, get_aes_gcm_data

URL = "https://wlc.nppa.gov.cn/test/collection/loginout/%s"


def test_case07(the_cfg, test_code):
    _url = URL % test_code

    headers = {
        "appId": the_cfg.app_id,
        "bizId": the_cfg.biz_id,
        "timestamps": str("%.3f" % time.time()).replace(".", ""),
    }
    data = {
        "collections": [
            {
                "no": 2,
                "si": "111",
                "bt": 0,
                "ot": 1615543517,
                "ct": 2,  # 0: 已认证 2: 游客
                "di": "111",
                "pi": "1fffbjzos82bs9cnyj1dna7d6d29zg4esnh99u",
            }
        ]
    }
    body = json.dumps(data)
    request_data_s = json.dumps({"data": get_aes_gcm_data(body, the_cfg.secret_key)})
    headers.update({
        "Content-Type": "application/json; charset=utf-8",
        "sign": get_sign(headers, request_data_s, the_cfg.secret_key)
    })
    res = requests.post(_url, data=request_data_s, headers=headers)
    print(res.content)


def test_case08(the_cfg, test_code):
    _url = URL % test_code

    headers = {
        "appId": the_cfg.app_id,
        "bizId": the_cfg.biz_id,
        "timestamps": str("%.3f" % time.time()).replace(".", ""),
    }
    data = {
        "collections": [
            {
                "no": 2,
                "si": "111",
                "bt": 0,
                "ot": 1615543517,
                "ct": 0,  # 0: 已认证 2: 游客
                "di": "111",
                "pi": "1fffbjzos82bs9cnyj1dna7d6d29zg4esnh99u",
            }
        ]
    }
    body = json.dumps(data)
    request_data_s = json.dumps({"data": get_aes_gcm_data(body, the_cfg.secret_key)})
    headers.update({
        "Content-Type": "application/json; charset=utf-8",
        "sign": get_sign(headers, request_data_s, the_cfg.secret_key)
    })
    res = requests.post(_url, data=request_data_s, headers=headers)
    print(res.content)
