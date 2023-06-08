from service import SearchService, AbstractSearchAlgo, AbstractTextsStorage


class StubStorage(AbstractTextsStorage):
    def get_texts(self) -> list[str]:
        return ["Inversion of Control"]


class StubAlgo(AbstractSearchAlgo):
    def match_best(self, text: str, corpus: list[str]):
        if corpus == ["Inversion of Control"]:
            return "Inversion of Control"
        raise NotImplementedError()



def test_serivce():
    search_service = SearchService(StubStorage(), StubAlgo()) # Еще и mypy не ругается, красота
    assert search_service.search("IoC") == "Inversion of Control"


# С интеграционными также как и в наивном примере
from .main import build_service

def integration_test():
    service = build_service()
    assert isinstance(service.search_service.search("IoC"), str)
