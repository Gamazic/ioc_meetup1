import os

from .controller import route
from .service import SearchService
from .storage import TextsDb
from .search_algo import SearchAlgo


def build_service():
    session = SomeSession(os.environ["DB_URL"])
    storage = TextsDb(session)
    search_algo = SearchAlgo()
    service = SearchService(storage, search_algo)
    return service


def main():
    app = FrameworkApp()
    app.add_route(route)
    app.override_dependency[SearchService] = build_service()
    app.start()
