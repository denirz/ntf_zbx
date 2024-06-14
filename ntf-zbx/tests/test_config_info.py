import pytest
import os

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


def test_config_info(capfd,create_config):
    currentdir = os.path.abspath(os.curdir)
    from ntf_zbx import config
    config.config_reload()
    config.config_info()
    resout = capfd.readouterr().out
    print(resout)
    print(currentdir)
    assert resout.find(currentdir) >= 0

def test_checkalias(capfd):
    #
    from ntf_zbx import ci
    ci()
    resout  = capfd.readouterr().out
    print(resout)  #  print(resout)
