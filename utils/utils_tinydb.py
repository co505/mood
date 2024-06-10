from tinydb import TinyDB, Query
from usr_info.user import logged_in_user
from usr_info.user import user_template
import datetime
import os


db = None
mood_table = None
query = Query()
dt_now = str(datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))


def initialize_db():
    global db, mood_table
    if not os.path.exists(f"{logged_in_user}_mood.json"):
        db = TinyDB(f"{logged_in_user}_mood.json")
        mood_table = db.table('mood')
        mood_table.insert({'File Created': dt_now})
    else:
        db = TinyDB(f"{logged_in_user}_mood.json")
        mood_table = db.table('mood')


def write_mood_date(score):
    mood_table.insert({'datetime': dt_now, 'score': score})

