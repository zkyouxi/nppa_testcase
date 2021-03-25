"""用户实名上传接口"""

import click

from util import make_request


URL = 'https://wlc.nppa.gov.cn/test/authentication/check/%s'


def test_case01(the_cfg):
    """
    断言
    1. 请求成功 errcode == 0
    2. 实名认证结果(认证成功) data.result.status == 0
    """
    test_code = click.prompt('\t>>> 请输入《testcase01-实名认证接口》测试码', type=str)
    url = URL % test_code
    data = {
        "ai":"100000000000000001",
        "name":"某一一",
        "idNum":"110000190101010001"
    }
    response = make_request(url, data, the_cfg)
    result = response.json()
    assert result["errcode"] == 0 and result["data"]["result"]["status"] == 0


def test_case02(the_cfg):
    """
    断言
    1. 请求成功 errcode == 0
    2. 实名认证结果(认证中) data.result.status == 1
    """
    test_code = click.prompt('\t>>> 请输入《testcase02-实名认证接口》测试码', type=str)
    url = URL % test_code
    data = {
        "ai":"200000000000000001",
        "name":"某二一",
        "idNum":"110000190201010009"
    }
    response = make_request(url, data, the_cfg)
    result = response.json()
    assert result["errcode"] == 0 and result["data"]["result"]["status"] == 1


def test_case03(the_cfg):
    """
    断言
    1. 请求成功 errcode == 0
    2. 实名认证结果(认证失败) data.result.status == 2
    """
    test_code = click.prompt('\t>>> 请输入《testcase03-实名认证接口》测试码', type=str)
    url = URL % test_code
    data = {
        "ai":"200000000000000009",
        "name":"某二九",
        "idNum":"110000190201040013"
    }
    response = make_request(url, data, the_cfg)
    result = response.json()
    assert result["errcode"] == 0 and result["data"]["result"]["status"] == 2
