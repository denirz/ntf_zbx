import os

import pytest


# from ntf_zbx import config
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

def create_2_config(command_text="cmd = echo  \"{item} {text}\""):
        act_conf = f"""
    ## Config.ini required for tests
    [Sender]
    ;cmd = 'ls'
    {command_text}
    ;FailOnError = False
    Timeout = 60
    DebugLevel=5
        """
        with open("./act_conf.ini", "w", encoding="utf-8") as f:
            f.write(act_conf)
        # yield "create_config"
        # os.remove("act_conf.ini")


def test_config_reload(create_config):
    import ntf_zbx
    from ntf_zbx import config
    ntf_zbx.ci()
    # change config
    create_2_config()
    assert config.config_reload() == 0
    ntf_zbx.ci()


@pytest.mark.skip(reason="not implemented")  # TODO: implemet config reload
def test_configreload_from_default():
    "reload config from default"
    try:
        os.remove("./act_conf.ini")
        print("config removed")
    except FileNotFoundError:
        pass
    create_2_config(command_text="ls -lR")
    print(os.listdir("."))
    os.system("cat ./act_conf.ini")
    import ntf_zbx

    # import importlib
    # importlib.reload(ntf_zbx)
    from ntf_zbx import config
    ntf_zbx.ci()
    origline = ntf_zbx.config.CP.get("Sender", "cmd")

    # change config
    create_2_config()
    assert config.config_reload() == 0
    ntf_zbx.ci()
    newline = ntf_zbx.config.CP.get("Sender", "cmd")
    print(origline, newline)
    assert origline != newline
