"""游戏用户行为数据上报接口"""

import click
import time

from util import make_request

URL = "https://wlc.nppa.gov.cn/test/collection/loginout/%s"


def test_case07(the_cfg):
    """testcase07-游戏用户行为数据上报接口

    游客行为上报
    """
    test_code = click.prompt('\n>>> 请输入《testcase07-游戏用户行为数据上报接口》测试码', type=str)
    url = URL % test_code

    data = {
        "collections": [{
            "no": 1,
            "si": "sessionid_1000101",
            "bt": 0,  # 0 下线 1 上线
            "ot": int(time.time()),
            "ct": 2,  # 2 游客
            "di": "youke_10010231",
            "pi": "1fffbjzos82bs9cnyj1dna7d6d29zg4esnh99u",
        }]
    }

    response = make_request(url, data, the_cfg)
    result = response.json()
    assert result["errcode"] == 0


def test_case08(the_cfg):
    """testcase08-游戏用户行为数据上报接口

    认证用户行为上报
    """
    test_code = click.prompt('\n>>> 请输入《testcase08-游戏用户行为数据上报接口》测试码', type=str)
    url = URL % test_code

    data = {
        "collections": [{
            "no": 1,
            "si": "sessionid_1000101",
            "bt": 0,  # 0 下线 1 上线
            "ot": int(time.time()),
            "ct": 0,  # 2 已认证用户
            "di": "youke_10010231",
            "pi": "1fffbjzos82bs9cnyj1dna7d6d29zg4esnh99u",
        }]
    }

    response = make_request(url, data, the_cfg)
    result = response.json()
    assert result["errcode"] == 0
