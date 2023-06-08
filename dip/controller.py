from .service import SearchService


route = FrameworkRoute()


@route.get("/")
def search_handler(query: str, search_service: SearchService = Depends()):
    return search_service.search(query)
