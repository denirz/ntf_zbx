import pytest
# from ntf_zbx import config
from .test_config_info import create_config

def create_2_config():
        act_conf = """
    ## Config.ini required for tests
    [Sender]
    ;cmd = 'ls'
    ;cmd = echo {item} {text} aaa  >> testfile
    # cmd = lss -la {item} {text}
    # cmd = pwd; ls  {item} {text};
    cmd = lldreload  {item} "{text}"
    ;FailOnError = False
    Timeout = 60
    DebugLevel=10
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
    assert config.config_reload()== 0
    ntf_zbx.ci()

def test_configreload_from_default():
    "reload config from default"
    import ntf_zbx
    from ntf_zbx import config
    ntf_zbx.ci()
    # change config
    create_2_config()
    assert config.config_reload() == 0
    ntf_zbx.ci()
    pass