from functools import wraps
from tinydb import TinyDB, Query
from usr_info.user import logged_in_user
import datetime
import os


query = Query()
dt_now = str(datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))
db = TinyDB(f"{logged_in_user}_mood.json")
mood_table = db.table('mood')


def delete_mood_data():
    if os.path.exists(f"{logged_in_user}_mood.json"):
        os.remove(f"{logged_in_user}_mood.json")


def write_mood_data(datetime_now, score):
    mood_table.insert({'datetime': datetime_now, 'score': score})

# def retrieve_mood_date():
#     initialize_db()
#     db.search()
