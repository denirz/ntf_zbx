import configparser
from unittest import TestCase
import os
import shutil
CONFIGTEMPLATE = "config.ini.incorrect"
CONFIGTEMPLATE = "config.ini.correct"


class TestConfig(TestCase):
    def setUp(self) -> None:
        shutil.move(CONFIGTEMPLATE, "config.ini")
        from ntf_zbx.config import CP
        self.CP = CP
        pass

    def tearDown(self) -> None:
        shutil.move("config.ini", CONFIGTEMPLATE)
        pass

    def test_configparser(self):
        self.assertIsInstance(self.CP, configparser.ConfigParser)
        # print(CP.sections())
        self.assertIn(
            "Sender", self.CP.sections(), "Section _Sender_ not found in config.ini"
        )

    def test_commandvalidity(self):
        from ntf_zbx.config import check_cmd
        result = check_cmd()
        print(result)
        self.assertTrue(result)