"""用户实名上传接口"""

import json
import time
import requests

from util import get_sign, get_aes_gcm_data

url = "https://wlc.nppa.gov.cn/test/authentication/check/%s"

def test_case01(the_cfg):
    code = "testcase01"
    test_url = url % code

    headers = {
        "appId": the_cfg.app_id,
        "bizId": the_cfg.biz_id,
        "timestamps": str("%.3f" % time.time()).replace(".", ""),
    }
    data = {
        "ai": "this_is_a_test_ai",
        "name": "test_name",
        "idNum": "test_idnum"
    }
    body = json.dumps(data, separators=(',',':'))

    request_data_s = json.dumps({"data": get_aes_gcm_data(body, the_cfg.secret_key)}, separators=(',',':'))
    headers.update({
        "Content-Type":"application/json; charset=utf-8",
        "sign": get_sign(headers, request_data_s, the_cfg.secret_key)
    })
    print(test_url)
    print(request_data_s)
    print(headers)

    res = requests.post(test_url, data=request_data_s, headers=headers)
    print(res.status_code)
    print(res.content)
