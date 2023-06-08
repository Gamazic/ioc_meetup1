from .storage import texts_db
from .search_algo import search_algo


class SearchService:
    def search(self, text: str) -> str:
        """returns Top 1 matched text from corpus"""
        texts_corpus = texts_db.get_texts()
        return search_algo.match_best(text, texts_corpus)


search_service = SearchService()