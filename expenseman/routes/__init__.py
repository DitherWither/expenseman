from flask import Blueprint
from .hello import blueprint as hello_blueprint

blueprint = Blueprint("app", __name__, url_prefix="/")

blueprint.register_blueprint(hello_blueprint, url_prefix="/hello")
