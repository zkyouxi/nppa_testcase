from collections import namedtuple

Cfg = namedtuple("Cfg", ["app_id", "secret_key", "biz_id"])

__FK_CFG = Cfg(
    "134fc9294cbe4583bf12d8d9062ecc34",
    "319565fe81b5b4376fd0c52eb44b803d",
    "1101999999"
)


def get_config(co_name: str) -> Cfg:
    co_name_upper = co_name.upper()
    key = "__%s_CFG" % co_name_upper
    return globals().get(key)
