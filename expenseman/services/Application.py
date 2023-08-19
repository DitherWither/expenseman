from .PgService import PgService
from flask import g
from ..config import Config


class Application:
    pg_service: PgService

    def __init__(self) -> None:
        self.pg_service = PgService(Config.POSTGRES_CONNECTION_STRING)

    def close(self):
        self.pg_service.close()


def get_app() -> Application:
    if "app" not in g:
        g.app = Application()

    return g.app


def close_app():
    app = g.pop("app", None)

    if app is not None:
        app.close()
