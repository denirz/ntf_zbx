"""
Read config an defined CP object with all reauilred config data
"""

import os
from configparser import ConfigParser

filedir = os.path.dirname(os.path.abspath(__file__))
curdir = os.path.abspath(os.curdir)
CP = ConfigParser()

configfound = False
for p in [
    curdir,
    filedir,
]:
    filename = os.path.join(p, "act_conf.ini")
    try:
        with open(os.path.join(p, "act_conf.ini"), encoding="utf-8") as f:
            CP.read_file(f)
            configfound = True
            break
    except FileNotFoundError:
        continue
if not configfound:
    raise FileNotFoundError


def check_cmd():
    """
    returns True if command exists and executable
    :return:
    """
    cmd = CP.get("Sender", "cmd").strip("'")
    for f in os.environ["PATH"].split(":"):
        try: # TODO: Seems to be fixed and tested specially
            if cmd in os.listdir(f):
                return True  # TODO: add checks if file is executable
        except FileNotFoundError:
            pass
    return False
