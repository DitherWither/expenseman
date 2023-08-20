from flask import redirect, session, url_for
from functools import wraps


def needs_login(func):
    @wraps(func)
    def check_login(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("app.auth.login_get"))
        return func(*args, **kwargs)

    return check_login
