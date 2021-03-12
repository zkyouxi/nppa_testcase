import click

from cfg import get_config
from test_identity_post import *
from test_identity_query import *
from test_behavior_collection import *


@click.command()
@click.option("test_case", "-n", default='')
@click.option("config", "-c", default='fk')
@click.option("test_code", "-m", default='')
def main(test_case, config, test_code):
    cfg = get_config(config)
    eval(test_case)(cfg, test_code)


if __name__ == "__main__":
    main()
