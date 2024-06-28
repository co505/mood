from tinydb import TinyDB, Query
import datetime
import os


def initialize_db(db_path):
    return TinyDB(db_path)


def first_db_setup(db, name, datetime, score):
    return db.insert({'Name': name, 'Datetime': datetime, 'Score': score})


def get_datetime():
    return datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")


def db_path_exists(db_path):
    return True if os.path.exists(db_path) else False


def delete_mood_data(db_path): # Can we use the db_path_exists function as a varaible here?
    if os.path.exists(db_path):
        return os.remove(db_path)
    else:
        return "Oops, no such user is available."


def write_mood_data(db, score) -> None:
    mood_table = db.table('mood')
    mood_table.insert({'datetime': get_datetime(), 'score': score})


