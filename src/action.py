import os

try:
    from jk_git import *
except:
    print("jk_git not available")
else:
    print("jk_git available")

github_output_env = os.environ.get('GITHUB_OUTPUT', "NOT-SET")
print("Hello World! {}".format(github_output_env))
