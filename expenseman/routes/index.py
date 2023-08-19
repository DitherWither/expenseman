from flask import Blueprint, render_template
from ..services.Application import get_app
blueprint = Blueprint("index", __name__)


@blueprint.get("/")
def index():
    return render_template("index.html.jinja2")
