import os
from dataclasses import dataclass


@dataclass
class User(frozen=True):
    name: str
    score: int

    @property
    def name(self):
        return self.name

    @property
    def score(self):
        return self.score



