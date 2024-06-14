from ntf_zbx import zs


def test_zs():
    """
    проверяем что работает  импорт zs
    :return:
    """
    res = zs(item="Item1", text="какой-то глупый текст")
    assert res == 0
