from tinydb import TinyDB, Query
import datetime
import os
import usr_info


query = Query()
dt_now = str(datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))
db = TinyDB(f"{usr_info.logged_in_user}_mood.json")
mood_table = db.table('mood')


def delete_mood_data():
    if os.path.exists(f"{usr_info.logged_in_user}_mood.json"):
        os.remove(f"{usr_info.logged_in_user}_mood.json")


def write_mood_data(datetime_now, score):
    mood_table.insert({'datetime': datetime_now, 'score': score})

# def retrieve_mood_date():
#     initialize_db()
#     db.search()
