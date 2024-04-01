from config import CP
import subprocess


def call_action(text, *args, **kwargs):
    command = CP.get("Sender", "cmd").strip("'")
    print(command)
    res = subprocess.run([command], capture_output=True)
    # print(res.stdout)
    if res.returncode != 0:
        print(res.stdout, res.stderr)
