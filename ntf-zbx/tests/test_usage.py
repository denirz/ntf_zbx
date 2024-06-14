from ntf_zbx import cmdsender
# from ntf_zbx import zs

def test_call():
    res = cmdsender.call_action(item="11", text="some text")
    # res = zs(item="11", text="some text")
    print(res)
    assert res == 0
