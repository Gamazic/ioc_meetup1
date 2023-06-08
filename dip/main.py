import os

from .controller import route
from .service import SearchService
from .storage import TextsDb, TextsStorageSuperFast
from .search_algo import RandomizedAlgo


def build_service():
    session = SomeSession(os.environ["DB_URL"])
    storage = TextsDb(session)
    search_algo = RandomizedAlgo()
    service = SearchService(storage, search_algo)
    return service


# def build_service_super_fast():
#     session = SomeSession(os.environ["DB_URL"])
#     storage = TextsStorageSuperFast(session)  # Вот там меняем зависимость
#     search_algo = RandomizedAlgo()
#     service = SearchService(storage, search_algo)
#     return service


def main():
    app = FrameworkApp()
    app.add_route(route)
    app.override_dependency[SearchService] = build_service()
    # app.override_dependency[SearchService] = build_service_super_fast()
    app.start()
