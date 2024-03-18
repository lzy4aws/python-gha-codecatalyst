# Git functionallity for Python. Included in src/requirements.txt.
from jk_git import *
# GitHub functionallity for Python. Included in src/requirements.txt. Fore more information, please see:
# https://github.blog/2020-12-18-learn-about-ghapi-a-new-third-party-python-client-for-the-github-api/
from ghapi.core import GhApi
GH = GhApi()
                              # Start of Action #
# A simple "Hello, World!" action.
#
# Replace the entire content of this file with your own content, except the first 6 lines.
# After replacing the code, that code will be executed when the Actions workflow
# starts this action.
print("Hello World!")
