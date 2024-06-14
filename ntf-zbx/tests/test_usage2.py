import logging
import os
import importlib

import pytest

@pytest.fixture
def remove_config():
    if os.path.isfile("act_conf.ini"):
        os.remove("act_conf.ini")




@pytest.fixture
def create_config():
    act_conf = """
## Config.ini required for tests
[Sender]
;cmd = 'ls'
;cmd = echo {item} {text} aaa  >> testfile
# cmd = lss -la {item} {text}
# cmd = pwd; ls  {item} {text};
cmd = ls  {item} "{text}"
;FailOnError = False
Timeout = 60
DebugLevel=10
    """
    with open("./act_conf.ini", "w", encoding="utf-8") as f:
        f.write(act_conf)
    yield "create_config"
    os.remove("act_conf.ini")

def test_somedata(create_config,caplog):
    # assert "act_conf.ini" not in os.listdir(os.curdir);
    caplog.set_level(10)
    importlib.invalidate_caches()
    from ntf_zbx.cmdsender import call_action
    res = call_action("-R", ".")
    print(caplog.text)
    assert res == 0



def test_runwithconf(create_config, caplog):
    # print(caplog.__dir__())
    print(os.curdir)
    with open("./act_conf.ini",'r') as f:
        print(f.read())
    # print(os.listdir(os.curdir))
    assert "act_conf.ini" in os.listdir(os.curdir);

    importlib.invalidate_caches()
    from ntf_zbx.cmdsender import call_action

    caplog.set_level(10)
    res = call_action("-la", "/Users/denirz/Documents/Travels/Uzbekistan 05 24")
    logging.info("greet me! ")
    print(caplog.text)
    assert res == 0
