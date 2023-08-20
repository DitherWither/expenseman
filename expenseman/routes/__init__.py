from flask import Blueprint
from .index import blueprint as index_blueprint
from .auth import auth_blueprint

blueprint = Blueprint("app", __name__, url_prefix="/")

blueprint.register_blueprint(index_blueprint, url_prefix="/")
blueprint.register_blueprint(auth_blueprint, url_prefix="/auth")
