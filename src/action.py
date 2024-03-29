import os
import pathlib
from datetime import datetime

try:
    from actions_toolkit import core
except:
    print("actions toolkit core not available")
else:
    print("core available")


def set_output(key: str, value: str):
    file_path = os.getenv("GITHUB_OUTPUT")
    if not file_path:
        raise Exception(f"Unable to find output file GITHUB_OUTPUT")
    if not pathlib.Path(file_path).exists():
        raise Exception(f"Missing file at path: {file_path}")
    os.system(f"echo {key.upper()}={value} >> {file_path}")


# Receive the inputs
who_to_greet = core.get_input('who-to-greet', required=True)
print("Hello {}!".format(who_to_greet))

github_output_env = os.environ.get('GITHUB_OUTPUT', "NOT-SET")
github_input_env = os.environ.get('INPUT_WHO-TO-GREET', "NOT-SET")

print("Env GITHUB_OUTPUT: {}\nINPUT_WHO-TO-GREET: {}".format(github_output_env, github_input_env))

# Return the outputs
# set_output("TIME", datetime.now().strftime("%A, %B %d, %Y %I:%M:%S %p"))
set_output("TIME", "green")

file_path = os.getenv("GITHUB_OUTPUT")
with open(file_path, "r", encoding="utf8", newline="") as f:
    print(f.read(), end="")
