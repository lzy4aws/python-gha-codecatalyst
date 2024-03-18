import os

try:
    from actions_toolkit import core
except:
    print("actions toolkit core not available")
else:
    print("core available")

# Receive the inputs
who_to_greet = core.get_input('who-to-greet', required=True, trim_whitespace=True)
print("hi {}! Hello World to you!".format(who_to_greet))


github_output_env = os.environ.get('GITHUB_OUTPUT', "NOT-SET")
github_input_env = os.environ.get('INPUT_WHO-TO-GREET', "NOT-SET")

print("Env GITHUB_OUTPUT: {}\nINPUT_WHO-TO-GREET: {}".format(github_output_env, github_input_env))

# Return the outputs
core.set_output('my_response', 'You too!')
