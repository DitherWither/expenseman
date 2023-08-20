from flask import Blueprint, render_template
from ..services.Application import get_app
from ..services.utils import needs_login
blueprint = Blueprint("index", __name__)


@blueprint.get("/")
@needs_login
def index():
    return render_template("index.html.jinja2")
