import psycopg
from urllib.parse import urlparse


class PgService:
    connection_string: str
    conn: psycopg.connection

    def __init__(self, connection_string: str) -> None:
        self.connection_string = connection_string
        self.conn = psycopg.connect(connection_string)

    def close(self):
        self.conn.close
