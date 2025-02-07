from utils.cli_interaction import cli, welcome
import os
from usr.user import User

if __name__ == "__main__":
    # A new file is created to track when the user first starts the application.
    # We cannot use the json file as the file creation seems to be executed before main is called.
    # Meaning, we can't check for the non-existence of a file if it's existence is created before we can check.
    if not os.path.exists("user.txt"):
        fp = open("user.txt", 'x')
        fp.close()
        welcome()
    else:
        cli()

