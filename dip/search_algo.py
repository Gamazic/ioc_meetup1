import random

from .service import AbstractSearchAlgo


class RandomizedAlgo(AbstractSearchAlgo):
    def match_best(self, text: str, corpus: list[str]) -> str:
        return random.choice(corpus)

