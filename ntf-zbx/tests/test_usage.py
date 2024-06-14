import pytest
import os
from ntf_zbx import cmdsender

# from ntf_zbx import zs
@pytest.fixture()
def deleteconfig():
    try:
        os.remove("act_conf.ini")
    except FileNotFoundError:
        pass
    return "deleteconfig"


def test_call(caplog,deleteconfig):
    caplog.set_level(10)
    cmdsender.call_action(item="11", text="some text")
    res = cmdsender.call_action(item="11", text="some text")
    # res = zs(item="11", text="some text")
    print(res)
    assert res == 0
