from abc import ABC, abstractmethod


class AbstractTextsStorage(ABC):
    @abstractmethod
    def get_texts(self) -> list[str]:
        pass


class AbstractSearchAlgo(ABC):
    @abstractmethod
    def match_best(self, text: str, corpus: list[str]) -> str:
        pass


class SearchService:
    def __init__(self, storage: AbstractTextsStorage, search_algo: AbstractSearchAlgo):
        self._storage = storage
        self._search_algo = search_algo

    def search(self, text: str) -> str:
        """returns Top 1 matched text from corpus"""
        texts_corpus = self._storage.get_texts()
        return self._search_algo.match_best(text, texts_corpus)
