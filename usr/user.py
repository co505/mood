import json
from cryptography.fernet import Fernet
import os

key = Fernet.generate_key()
cipher_suite = Fernet(key)

user_data = {
    'user': 'username',
    'email': cipher_suite.encrypt(b'user@example.com').decode(),
    'settings': {
        'theme': 'dark',
        'autosave': True
    }
}