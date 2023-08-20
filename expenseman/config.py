import os


class Config:
    POSTGRES_CONNECTION_STRING = os.environ.get("POSTGRES_CONNECTION_STRING")
    PORT = os.environ.get("PORT") or 8080
    SECRET_KEY = os.environ.get("SECRET_KEY")
