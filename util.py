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
    secret_key_pre16 = secret_key[:16]
    key = secret_key_pre16.encode("utf8")
    cipher = AES.new(key, AES.MODE_GCM)
    encrypted_data = cipher.encrypt(pad(body.encode("utf8"), AES.block_size))
    # ciphertext, tag = cipher.encrypt_and_digest(body.encode("utf8"))
    # ciphertext = ciphertext + tag
    return base64.b64encode(encrypted_data).decode("utf8")
