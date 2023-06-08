from .controller import route


def main():
    app = FrameworkApp()
    app.add_route(route)
    app.start()
