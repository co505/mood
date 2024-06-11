from utils.utils_click import cli, welcome
import datetime
import os
from usr_info.user import logged_in_user

if __name__ == "__main__":
    if not os.path.exists(f"{logged_in_user}.txt"):
        # A new file is created to track when the user first starts the application.
        # We cannot use the json file as the file creation seems to be executed before main is called.
        # Meaning, we can't check for the non-existence of a file if it's existence is created before we can check.
        fp = open(f"{logged_in_user}.txt", 'x')
        fp.close()
        welcome()
    else:
        cli()