import logging
import subprocess

from ntf_zbx.config import CP

logging.basicConfig(level=logging.INFO)


def call_action(item="", text="", timeout=CP.getint("sender", "Timeout", fallback=60)):
    """
    Main Function to call
    :param text:
    :param args:
    :param kwargs:
        :param timeout: Timeout (s) to kill command after.
    :return:
    """
    command = CP.get("Sender", "cmd").strip("'")
    try:
        command = command.format(text=text, item=item)
    except KeyError:
        logging.warning(f"Error in data {text},{item}: {command}")
        if CP.getboolean("Sender", "FailOnError", fallback=False):
            raise ValueError
    command = command.split(" ")
    logging.debug(f"Running {command}...")
    try:
        res = subprocess.run(command, capture_output=True, timeout=timeout, check=False)
        logging.warning(f"stdout = \n{res.stdout.decode()}")
        # print("stdout = \n{}".format(res.stdout.decode()))
        if res.returncode != 0:
            logging.debug(f"returncode = {res.returncode}")
            logging.debug(f"stderr = {res.stderr.decode()}")
        return res.returncode
    except FileNotFoundError:
        logging.warning(f"something wrong with {command}")
    except subprocess.TimeoutExpired:
        logging.warning(f"Timeout {timeout} expired with {command}")
