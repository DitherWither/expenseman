import os


class Config:
    POSTGRES_CONNECTION_STRING = os.environ.get("POSTGRES_CONNECTION_STRING")
    PORT = os.environ.get("PORT") or 8080
