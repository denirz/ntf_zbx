import logging
import os

import pytest


def test_somedata():
    from ntf_zbx.cmdsender import call_action

    res = call_action("d", "t")
    assert res == 0


@pytest.fixture
def create_config():
    act_conf = """
## Config.ini required for tests
[Sender]
;cmd = 'ls'
;cmd = echo {item} {text} aaa  >> testfile
cmd = ls -la
;FailOnError = False
Timeout = 60
    """
    with open("act_conf.ini", "w", encoding="utf-8") as f:
        f.write(act_conf)
    yield
    os.remove("act_conf.ini")


def test_runwithconf(create_config, caplog):
    # print(caplog.__dir__())
    from ntf_zbx.cmdsender import call_action

    caplog.set_level(logging.INFO)
    res = call_action("dR", "t")
    logging.info("greet me! ")
    assert res == 0
