from ntf_zbx import zs
import datetime
import pytest
testdata = [
    ("IntergationEvents","aaa"),
    ("IntergationEvents","aaa\nbbb"),
    ("IntergationEvents","ntf_zbx-0.1.0-py3-none-any.whl successfully installed\n\n{}".format(datetime.datetime.now().isoformat())),
]

@pytest.mark.parametrize("item,text", testdata )
def test_send(item,text):
    res = zs(item=item, text=text)
    assert res ==0