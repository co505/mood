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
