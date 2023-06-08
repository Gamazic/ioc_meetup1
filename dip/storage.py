from .service import AbstractTextsStorage


class TextsDb(AbstractTextsStorage):
    def __init__(self, session):
        self.session = session

    def get_texts(self) -> list[str]:
        result = self.session.execute("SELECT ... FROM texts").fetchall()
        return list(result)


# А потом очень легко расширить систему
class TextsStorageSuperFast(AbstractTextsStorage):
    def __init__(self, redis: Redis):
        self._redis = redis

    def get_texts(self) -> list[str]:
        return self._redis.get("ALL_TEXTS")
