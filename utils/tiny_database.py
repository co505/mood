from tinydb import TinyDB, Query
from usr_info.user import logged_in_user
from usr_info.user import user_template


db = TinyDB(f'{logged_in_user}_mood.json')
mood_table = db.table('mood')
query = Query()


def create_structure():
    mood_table.insert(user_template)


def write_mood_date(datetime, score):
    mood_table.insert({'datetime': datetime, 'score': score})

