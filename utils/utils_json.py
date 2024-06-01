import json
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

with open('mood_data.json', 'w') as jsonfile:
    json.dump(mood_data, jsonfile)

# Set file permissions to read/write for the owner only
os.chmod('user_data.json', 0o600)