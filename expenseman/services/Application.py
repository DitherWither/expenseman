from .PgUserService import PgUserService
from .PgService import PgService
from flask import g
from .UserService import UserService
from ..config import Config


class Application:
    pg_service: PgService
    user_service: UserService

    def __init__(self) -> None:
        self.pg_service = PgService(Config.POSTGRES_CONNECTION_STRING)
        self.user_service = PgUserService(self.pg_service.conn)

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
