"""用户实名上传接口"""

import json
import time

import requests

from util import get_sign, get_aes_gcm_data


URL = 'https://wlc.nppa.gov.cn/test/authentication/check/%s'


def test_case01(the_cfg, test_code):
    _url = URL % test_code

    headers = {
        "appId": the_cfg.app_id,
        "bizId": the_cfg.biz_id,
        "timestamps": str("%.3f" % time.time()).replace(".", ""),
    }
    data = {
        "ai": "this_is_a_test_ai",
        "name": "test_name",
        "idNum": "1111111111111"
    }
    body = json.dumps(data, separators=(',', ':'))
    request_data_s = json.dumps({"data": get_aes_gcm_data(body, the_cfg.secret_key)}, separators=(',', ':'))
    headers.update({
        "Content-Type": "application/json; charset=utf-8",
        "sign": get_sign(headers, request_data_s, the_cfg.secret_key)
    })
    res = requests.post(_url, data=request_data_s, headers=headers)
    print(res.content)
