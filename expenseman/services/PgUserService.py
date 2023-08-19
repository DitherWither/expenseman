from ..models import User
from .UserService import LoginError, UserCreateError, UserGetError
from . import UserService
import psycopg
from psycopg.rows import class_row
from werkzeug.security import generate_password_hash, check_password_hash


class PgUserService(UserService):
    conn: psycopg.Connection

    def __init__(self, conn: psycopg.Connection) -> None:
        self.conn = conn

    def get_all(self) -> list[User] | UserGetError:
        try:
            with self.conn.cursor(row_factory=class_row(User)) as cur:
                users = cur.execute("SELECT id, email, password FROM users").fetchall()
                return users
        except psycopg.Error:
            return UserGetError.DATABASE_ERROR

    def get_by_id(self, id: str) -> User | UserGetError:
        try:
            with self.conn.cursor(row_factory=class_row(User)) as cur:
                user = cur.execute(
                    "SELECT id, email, password FROM users WHERE id = %s", (id,)
                ).fetchone()

                if user is None:
                    return UserGetError.USER_DOES_NOT_EXIST
                else:
                    return user
        except psycopg.Error:
            return UserGetError.DATABASE_ERROR

    def get_by_email(self, email: str) -> User | UserGetError:
        try:
            with self.conn.cursor(row_factory=class_row(User)) as cur:
                user = cur.execute(
                    "SELECT id, email, password FROM users WHERE email = %s", (email,)
                ).fetchone()

                if user is None:
                    return UserGetError.USER_DOES_NOT_EXIST
                else:
                    return user
        except psycopg.Error:
            return UserGetError.USER_DOES_NOT_EXIST

    def create_new(self, user: User) -> User | UserCreateError:
        if self.get_by_email(user.email) != UserGetError.USER_DOES_NOT_EXIST:
            return UserCreateError.EMAIL_ALREADY_EXISTS

        if len(user.password) < 9:
            return UserCreateError.PASSWORD_TOO_SHORT

        # Hash our password
        password_hash = generate_password_hash(user.password)

        try:
            with self.conn.cursor(row_factory=class_row(User)) as cur:
                user = cur.execute(
                    "INSERT INTO users (email, password) VALUES (%s, %s) RETURNING id, email, password",
                    (user.email, password_hash),
                ).fetchone()

                self.conn.commit()
                if user is None:
                    return UserCreateError.UNKNOWN_ERROR
                else:
                    return user
        except psycopg.Error:
            return UserCreateError.DATABASE_ERROR

    def login(self, user: User) -> str | LoginError:
        match self.get_by_email(user.email):
            case UserGetError.USER_DOES_NOT_EXIST:
                return LoginError.USER_DOES_NOT_EXIST
            case UserGetError.DATABASE_ERROR:
                return LoginError.DATABASE_ERROR
            case db_user:
                if not check_password_hash(db_user.password, user.password):
                    return LoginError.INVALID_PASSWORD

                return db_user.id
