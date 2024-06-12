import os
import shutil
import unittest

import pytest

CONFIGFILE = "config.ini.correct"
# CONFIGFILE = "config.ini.incorrect"


@pytest.fixture(autouse=True)
def cwdto_test():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))


class Test_cmdserder_correct(unittest.TestCase):
    def setUp(self) -> None:
        print(f"Current Dir = {os.path.abspath(os.path.curdir)}")
        shutil.copy(CONFIGFILE, "act_conf.ini")
        from ntf_zbx import cmdsender

        self.cmdsender = cmdsender

    def tearDown(self) -> None:
        os.remove("act_conf.ini")
        # shutil.move("config.ini", CONFIGFILE)

    def test_cmdsender(self):
        self.cmdsender.call_action(item=".", text="")
        # self.assertEqual(True, False)  # add assertion here

    def testSenderwithtimeout(self):
        self.cmdsender.call_action(item=None, text="/", timeout=10)

    def testSenderwithText(self):
        self.cmdsender.call_action("..")

    def testSenderWithKwargs(self):
        self.cmdsender.call_action(item="..", text="asdd")


if __name__ == "__main__":
    unittest.main()
