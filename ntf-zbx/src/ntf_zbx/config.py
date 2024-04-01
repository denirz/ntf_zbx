"""
Read config an defined CP object with all reauilred config data
"""
import os
import sys
from configparser import ConfigParser
if not os.path.exists("../../config.ini"):
    print(os.environ['PATH'])
    print(os.environ['PYTHONPATH'])
    raise FileNotFoundError("config.ini not found!")

CP = ConfigParser()
CP.read(filenames="config.ini")



def check_cmd():
    """
    returns True if command exists and executable
    :return:
    """
    cmd = CP.get("Sender", "cmd").strip("'")
    for f in os.environ['PATH'].split(":"):
        if cmd in os.listdir(f):
            return True #todo add checks if file is executable
    return False

