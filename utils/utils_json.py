import json
from cryptography.fernet import Fernet

# key = Fernet.generate_key()
# cipher_suite = Fernet(key)


def create_mood_data(mood_data, file_path):
    with open(file_path, 'x') as jsonfile:
        json.dump(mood_data, jsonfile)


def write_mood_data(mood_data, file_path):
    with open(file_path, 'w') as jsonfile:
        json.dump(mood_data, jsonfile)


def retrieve_mood_data(file_path):
    with open(file_path, 'r') as jsonfile:
        mood_data = json.load(jsonfile)
        return mood_data

