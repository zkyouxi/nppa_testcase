import os
import base64
from hashlib import sha256

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

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
    iv = os.urandom(12)
    key = bytes.fromhex(secret_key)
    encryptor = AES.new(key=key, mode=AES.MODE_GCM, nonce=iv)
    ctx = encryptor.encrypt(body.encode('utf-8'))
    tag = encryptor.digest()
    return base64.b64encode(iv + ctx + tag).decode("utf8")
