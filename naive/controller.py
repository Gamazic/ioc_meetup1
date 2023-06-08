from .service import search_service


route = FrameworkRoute()


@route.get("/")
def search_handler(query: str):
    return search_service.search(query)
