from dataclasses import dataclass


class User:
    current_user = ""

    def __init__(self, name="Default", score=0):
        self.name = name
        self.score = score

    @classmethod
    def get_current_user(cls):
        return cls.current_user

    @classmethod
    def set_current_user(cls, x):
        cls.current_user = x



"""

    Static Variable, which will be set modified using a setter. 
    Static variable will contain the 'login' information for a particular user.
    Right now, we don't care for a password. 
    Getter will access the static variable
     
"""