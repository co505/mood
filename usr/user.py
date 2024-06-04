import json
from cryptography.fernet import Fernet
import os

key = Fernet.generate_key()
cipher_suite = Fernet(key)
user_info = {}
