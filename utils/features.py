import pandas as pd
import usr_info as user


def trial():
    json = pd.read_json(f"/home/connor/PycharmProjects/mood/{user.logged_in_user}_mood.json")
    print(json)
