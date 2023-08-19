from flask import Blueprint

blueprint = Blueprint("hello", __name__)

@blueprint.get("/")
def hello():
    return "Hello, World"
