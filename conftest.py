import os
import sys
import logging

import pytest

from cfg import get_config

_co_name = os.environ.get("CO_NAME")
if _co_name is None:
    logging.error("需要预设环境变量 CO_NAME")
    sys.exit(0)

cfg = get_config(_co_name)


@pytest.fixture
def the_cfg():
    yield cfg
