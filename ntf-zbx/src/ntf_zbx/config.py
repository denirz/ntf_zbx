"""
Read config an defined CP object with all reauilred config data
"""
import os
import sys
from configparser import ConfigParser


CP = ConfigParser()
CP.read(filenames="config.ini")


def check_cmd():
    """
    returns True if command exists and executable
    :return:
    """
    cmd = CP.get("Sender", "cmd").strip("'")
    for f in os.environ['PATH'].split(":"):
        # print(os.listdir(f))
        if cmd in os.listdir(f):
            return True #todo add checks if file is executable
    return False
    # print(os.environ['PYTHONPATH'])
    # for f in sys.path:
    #     print(f)
    #     print(os.listdir(f))
    # return cmd

