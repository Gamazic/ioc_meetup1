import service
import storage
import search_algo


class StubDb:
    def get_texts(self) -> list[str]:
        return ["Inversion of Control"]


class StubAlgo:
    def match_best(self, text: str, corpus: list[str]):
        if corpus == ["Inversion of Control"]:
            return "Inversion of Control"
        raise NotImplementedError()


def test_serivce():
    with patch(storage.texts_db, StubDb()):
        with patch(search_algo.search_algo, StubAlgo()):
            assert service.search_service.search("IoC") == "Inversion of Control"


# No Easy Unit Tests
# No way for tdd

# Easy only integro with dev
def integration_test():
    assert isinstance(service.search_service.search("IoC"), str)
