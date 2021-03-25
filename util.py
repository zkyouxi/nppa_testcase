import json
import time
import base64
from hashlib import sha256

import requests
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


the_timestamps = lambda : str("%.3f" % time.time()).replace(".", "")


def sort_dict_v(d):
    return "".join([
        "%s%s" % (
            i,
            sort_dict_v(j) if isinstance(j, dict) else j
        ) for i, j in
        sorted(d.items(), key=lambda m:m[0])
    ])


def get_sign(headers, body, secret_key):
    hs = sort_dict_v(headers)
    unhash_str = secret_key + hs + body
    return sha256(unhash_str.encode("utf8")).hexdigest()


def get_aes_gcm_data(body, secret_key):

    iv = get_random_bytes(12)
    key = bytes.fromhex(secret_key)
    encryptor = AES.new(key=key, mode=AES.MODE_GCM, nonce=iv)
    ctx = encryptor.encrypt(body.encode('utf-8'))
    tag = encryptor.digest()
    return base64.b64encode(iv + ctx + tag).decode("utf8")


def make_request(url, data, the_cfg, method="POST"):
    headers = {
        "appId": the_cfg.app_id,
        "bizId": the_cfg.biz_id,
        "timestamps": the_timestamps(),
    }
    post_data = {"data": get_aes_gcm_data(json.dumps(data), the_cfg.secret_key)}

    sign_headers = headers.copy()
    sign_body = json.dumps(post_data)
    if method == "GET":
        sign_headers.update(data)
        sign_body = ""

    headers.update({"sign": get_sign(sign_headers, sign_body, the_cfg.secret_key)})

    if method == "GET":
        return requests.get(url, params=data, headers=headers)

    return requests.post(url, json=post_data, headers=headers)
