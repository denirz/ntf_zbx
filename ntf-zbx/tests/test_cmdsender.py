import unittest
import shutil
CONFIGFILE = "config.ini.correct"
CONFIGFILE = "config.ini.incorrect"

class Test_cmdserder_correct(unittest.TestCase):
    def setUp(self) -> None:
        shutil.move(CONFIGFILE, "config.ini")
        from ntf_zbx import cmdsender

        self.cmdsender = cmdsender

    def tearDown(self) -> None:
        shutil.move("config.ini", CONFIGFILE)

    def test_cmdsender(self):
        self.cmdsender.call_action("Test call", severity="HIGH")
        # self.assertEqual(True, False)  # add assertion here


if __name__ == "__main__":
    unittest.main()
