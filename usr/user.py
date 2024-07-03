from dataclasses import dataclass


class User:

    def __init__(self, name="Default", score=0):
        self.name = name
        self.score = score

