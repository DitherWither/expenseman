from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from ..services.Application import get_app
from ..services.UserService import LoginError, UserCreateError
from ..models import User

auth_blueprint = Blueprint("auth", __name__)


@auth_blueprint.get("/login")
def login_get():
    if session.get("user_id"):
        return redirect("/")
    return render_template("login.html.jinja2")


@auth_blueprint.get("/signup")
def signup_get():
    if session.get("user_id"):
        return redirect("/")
    return render_template("signup.html.jinja2")


@auth_blueprint.post("/login")
def login_post():
    email = request.form["email"]
    password = request.form["password"]

    if not email:
        flash("Email is required")
        return redirect(url_for(".login_get"))
    if not password:
        flash("Password is required")
        return redirect(url_for(".login_get"))

    result = get_app().user_service.login(User("", email, password))

    if type(result) is LoginError:
        match result:
            case LoginError.DATABASE_ERROR:
                flash("Unknown database error occurred")
            case LoginError.USER_DOES_NOT_EXIST:
                flash(
                    "The user does not exist, please check if your email address is correct"
                )
            case LoginError.INVALID_PASSWORD:
                flash("Invalid Password, please check if password is correct")
        return redirect(url_for(".login_get"))
    else:
        session["user_id"] = result
        return redirect("/")


@auth_blueprint.post("/signup")
def signup_post():
    email = request.form["email"]
    password = request.form["password"]

    if not email:
        flash("Email is required")
        return redirect(url_for(".signup_get"))
    if not password:
        flash("Password is required")
        return redirect(url_for(".signup_get"))
    app = get_app()

    result = app.user_service.create_new(User("", email, password))

    if type(result) is UserCreateError:
        match result:
            case UserCreateError.DATABASE_ERROR:
                flash("Unknown database error occurred")
            case UserCreateError.EMAIL_ALREADY_EXISTS:
                flash("The email already exists, try logging in instead")
            case UserCreateError.PASSWORD_TOO_SHORT:
                flash("Password is too short, please pick a longer one")
            case UserCreateError.UNKNOWN_ERROR:
                flash("An unknown error occurred, please try again")
        return redirect(url_for(".signup_get"))
    else:
        session["user_id"] = result.id
        return redirect("/")


@auth_blueprint.post("/logout")
@auth_blueprint.get("/logout")
def logout():
    session.pop("user_id", None)
    return redirect("/")
