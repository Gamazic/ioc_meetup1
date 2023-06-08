from .storage import TextsDb
from .search_algo import SearchAlgo


class SearchService:
    def __init__(self, storage: TextsDb, search_algo: SearchAlgo):
        self._storage = storage
        self._search_algo = search_algo

    def search(self, text: str) -> str:
        """returns Top 1 matched text from corpus"""
        texts_corpus = self._storage.get_texts()
        return self._search_algo.match_best(text, texts_corpus)
