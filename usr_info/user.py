import os
from dataclasses import dataclass


#Data class provides a concise way to type out
@dataclass
class User(frozen=True):
    name: str
    score: int

logged_in_user = os.getlogin()


