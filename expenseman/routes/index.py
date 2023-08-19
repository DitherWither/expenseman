from flask import Blueprint, render_template

blueprint = Blueprint("index", __name__)

@blueprint.get("/")
def index():
    return render_template("index.html.jinja2")
