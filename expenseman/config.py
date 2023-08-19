import os


class Config:
    POSTGRES_URL = os.environ.get("POSTGRES_URL")
    PORT = os.environ.get("PORT") or 8080
