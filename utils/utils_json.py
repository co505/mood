import json
import os
from rich.console import Console

from cryptography.fernet import Fernet


# key = Fernet.generate_key()
# cipher_suite = Fernet(key)

console = Console()

# Use OS module for file management?


def create_mood_data(mood_data, file_path):
    try:
        with open(file_path, 'x') as jsonfile:
            json.dump(mood_data, jsonfile)
    except FileExistsError:
        return False


def write_mood_data(score, file_path):
    mood_data = {"score": score}
    try:
        with open(file_path, 'a+') as jsonfile:
            json.dump(mood_data, jsonfile)
    except Exception:
        print("shit")


def retrieve_mood_data(file_path):
    with open(file_path, 'r') as jsonfile:
        mood_data = json.load(jsonfile)
        return mood_data

