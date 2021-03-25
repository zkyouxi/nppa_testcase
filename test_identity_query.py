"""实名认证结果查询接口"""

import click

from util import make_request

URL = "https://wlc.nppa.gov.cn/test/authentication/query/%s"


def test_case04(the_cfg):
    test_code = click.prompt('\t>>> 请输入《testcase04-实名认证结果查询接口》测试码', type=str)
    url = URL % test_code

    data = {
        "ai": "100000000000000001"
    }

    response = make_request(url, data, the_cfg, method="GET")
    result = response.json()
    assert result["errcode"] == 0 and result["data"]["result"]["status"] == 0


def test_case05(the_cfg):
    test_code = click.prompt('\t>>> 请输入《testcase05-实名认证结果查询接口》测试码', type=str)
    url = URL % test_code

    data = {"ai":"200000000000000001"}

    response = make_request(url, data, the_cfg, method="GET")
    result = response.json()
    assert result["errcode"] == 0 and result["data"]["result"]["status"] == 1


def test_case06(the_cfg):
    test_code = click.prompt('\t>>> 请输入《testcase06-实名认证结果查询接口》测试码', type=str)
    url = URL % test_code

    data = {"ai":"300000000000000001"}

    response = make_request(url, data, the_cfg, method="GET")
    result = response.json()
    assert result["errcode"] == 0 and result["data"]["result"]["status"] == 2
