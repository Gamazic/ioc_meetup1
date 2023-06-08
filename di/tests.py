from service import SearchService


class StubDb:
    def get_texts(self) -> list[str]:
        return ["Inversion of Control"]


class StubAlgo:
    def match_best(self, text: str, corpus: list[str]):
        if corpus == ["Inversion of Control"]:
            return "Inversion of Control"
        raise NotImplementedError()



def test_serivce():
    search_service = SearchService(StubDB(), StubAlgo())
    assert search_service.search("IoC") == "Inversion of Control"
