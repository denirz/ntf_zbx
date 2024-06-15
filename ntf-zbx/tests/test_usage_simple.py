import pytest

def  test_runnoimport():
    """check for runwithout noimport"""
    text = "just a text"
    try:
        res = zs(item="IntergationEvents", text=text)
        assert res == 0
    except NameError:
        pass
