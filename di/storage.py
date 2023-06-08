class TextsDb:
    def __init__(self, session):
        self.session = session

    def get_texts(self) -> list[str]:
        result = self.session.execute("SELECT ... FROM texts").fetchall()
        return list(result)
