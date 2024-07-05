from tinydb import TinyDB, Query
import datetime
import os
from usr.user import User

JSON_FILE = f"{os.getlogin()}_mood.json"


def initialize_db():
    return TinyDB(JSON_FILE)


def first_db_setup(name, datetime, score):
    return TinyDB(JSON_FILE).insert({'Name': name, 'Datetime': datetime, 'Score': score})


def get_datetime():
    return datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")


def db_path_exists():
    return True if os.path.exists(JSON_FILE) else False


def delete_mood_data():
    if os.path.exists(JSON_FILE):
        return os.remove(JSON_FILE)
    else:
        return "Oops, no such user is available."


def write_mood_data(score) -> None:
    mood_table = TinyDB(JSON_FILE).table('mood')
    mood_table.insert({'datetime': get_datetime(), 'score': score})


