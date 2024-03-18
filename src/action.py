import os

try:
    from actions_toolkit import core
except:
    print("actions toolkit core not available")
else:
    print("core available")

who_to_greet = core.get_input('who-to-greet', required=True)
print("hi {}! Hello World to you!".format(who_to_greet))

github_output_env = os.environ.get('GITHUB_OUTPUT', "NOT-SET")
github_input_env = os.environ.get('INPUT_WHO_TO_GREET', "NOT-SET")

print("Env GITHUB_OUTPUT: {}\nINPUT_WHO_TO_GREET: {}".format(github_output_env, github_input_env))
