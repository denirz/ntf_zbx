from ntf_zbx import cmdsender


def test_call():
    res = cmdsender.call_action(item="11", text="some text")
    print(res)
    assert res == 0
