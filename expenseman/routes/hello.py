from flask import Blueprint, render_template

blueprint = Blueprint("hello", __name__)

@blueprint.get("/")
def hello():
    return render_template("hello.html.jinja2")
