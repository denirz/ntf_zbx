import configparser
import os
import shutil
import unittest
from unittest import TestCase

CONFIGTEMPLATE = "config.ini.incorrect"
CONFIGTEMPLATE = "config.ini.correct"


class TestConfig(TestCase):
    def setUp(self) -> None:
        shutil.copy(CONFIGTEMPLATE, "config.ini")
        from ntf_zbx.config import CP

        self.CP = CP

    def tearDown(self) -> None:
        shutil.move("config.ini", CONFIGTEMPLATE)

    def test_configparser(self):
        print(f"Current Directory = '{os.path.abspath(os.curdir)}'")
        self.assertIsInstance(self.CP, configparser.ConfigParser)
        self.assertIn(
            "Sender", self.CP.sections(), "Section _Sender_ not found in config.ini"
        )

    @unittest.skip
    def test_commandvalidity(self):
        from ntf_zbx.config import check_cmd

        result = check_cmd()
        print(result)
        self.assertTrue(result)


# from ntf_zbx.config import check_cmd


class TestConfigabsent(TestCase):
    """
    Running test with absent config
    """

    def setUp(self) -> None:
        print(f"Current Directory = '{os.path.abspath(os.curdir)}'")
        if os.path.isfile("/Users/denirz/Development/ntf_zbx/ntf-zbx/tests/config.ini"):
            os.remove("/Users/denirz/Development/ntf_zbx/ntf-zbx/tests/config.ini")
        if os.path.isfile(
            "/Users/denirz/Development/ntf_zbx/ntf-zbx/src/ntf_zbx/config.ini"
        ):
            os.remove(
                "/Users/denirz/Development/ntf_zbx/ntf-zbx/src/ntf_zbx/config.ini"
            )

    @unittest.skip
    def test_check_cmd_no_config(self):
        """
        If file is deleted - we should raise a arrer
        :return:
        """
        print(
            os.path.isfile("/Users/denirz/Development/ntf_zbx/ntf-zbx/tests/config.ini")
        )
        with self.assertRaises(FileNotFoundError):
            from ntf_zbx.config import CP
        with self.assertRaises(NameError):
            print(CP.sections())
