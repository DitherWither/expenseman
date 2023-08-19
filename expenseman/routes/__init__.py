from flask import Blueprint
from .index import blueprint as index_blueprint

blueprint = Blueprint("app", __name__, url_prefix="/")

blueprint.register_blueprint(index_blueprint, url_prefix="/")
