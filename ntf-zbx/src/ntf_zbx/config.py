"""
Read config an defined CP object with all reauilred config data
"""
import importlib
import logging
import os
from configparser import ConfigParser

filedir = os.path.dirname(os.path.abspath(__file__))
curdir = os.path.abspath(os.curdir)
CP = ConfigParser()


configfound = False
for p in (
    curdir,
    filedir,
):
    filename = os.path.join(p, "act_conf.ini")
    try:
        with open(os.path.join(p, "act_conf.ini"), encoding="utf-8") as f:
            CP.read_file(f)
            # print(f.read())
            configfound = True
            configlocation = os.path.join(p, "act_conf.ini")
            logging.debug(f"Config location = {configlocation}")
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
        try:  # TODO: Seems to be fixed and tested specially
            if cmd in os.listdir(f):
                return True  # TODO: add checks if file is executable
        except FileNotFoundError:
            pass
    return False

def config_reload():
    """
    Reloads config if module already loaded in memory
    """
    global configfound
    global configlocation
    global CP
    for p in (
            curdir,
            filedir,
    ):
        # filename = os.path.join(p, "act_conf.ini")
        try:
            with open(os.path.join(p, "act_conf.ini"), encoding="utf-8") as f:
                CP.read_file(f)
                # print(f.read())
                configfound = True
                configlocation = os.path.join(p, "act_conf.ini")
                logging.debug(f"Config location = {configlocation}")
                break
        except FileNotFoundError:
            continue
    if not configfound:
        raise FileNotFoundError
    if "ntf_zbx" in globals():
        importlib.reload(ntf_zbx)
    return 0


def config_info():
    """
    Displays config information

    """
    print(f"Config location  =  {configlocation}")
    for section in CP.sections():
        print(f"[{section}]")
        for key in CP[section]:
            print(f"{key} = {CP[section][key]}")


