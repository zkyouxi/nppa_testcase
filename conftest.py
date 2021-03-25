from collections import namedtuple

import click
import pytest

Cfg = namedtuple("Cfg", ["app_id", "secret_key", "biz_id"])

app_id = click.prompt('请输入 app_id', type=str)
secret_key = click.prompt('请输入 secret_key', type=str)
biz_id = click.prompt('请输入 biz_id', type=str)


@pytest.fixture(scope='session')
def the_cfg():
    yield Cfg(app_id, secret_key, biz_id)
