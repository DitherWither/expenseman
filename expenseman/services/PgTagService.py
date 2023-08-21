from expenseman.models import Tag
from expenseman.services.TagService import TagCreateError, TagGetError
from ..models import Tag
import psycopg
from psycopg.rows import class_row
from . import TagService, TagCreateError, TagGetError


class PgTagService(TagService):
    conn: psycopg.Connection

    def __init__(self, conn: psycopg.Connection) -> None:
        self.conn = conn

    def get_all(self) -> list[Tag] | TagGetError:
        try:
            with self.conn.cursor(row_factory=class_row(Tag)) as cur:
                tags = cur.execute("SELECT id, name, user_id FROM tags").fetchall()
                return tags
        except psycopg.Error:
            return TagGetError.DATABASE_ERROR

    def get_all_by_user(self, user_id: str) -> list[Tag] | TagGetError:
        try:
            with self.conn.cursor(row_factory=class_row(Tag)) as cur:
                tags = cur.execute(
                    "SELECT id, name, user_id FROM tags WHERE user_id = %s", (user_id,)
                ).fetchall()
                return tags
        except psycopg.Error:
            return TagGetError.DATABASE_ERROR

    def get_by_id(self, id: str) -> Tag | TagGetError:
        try:
            with self.conn.cursor(row_factory=class_row(Tag)) as cur:
                tag = cur.execute(
                    "SELECT id, name, user_id FROM tags WHERE id = %s", (id,)
                ).fetchone()

                if tag is None:
                    return TagGetError.TAG_DOES_NOT_EXIST
                return tag
        except psycopg.Error:
            return TagGetError.DATABASE_ERROR

    def get_by_id_checked(self, id: str, user_id: str) -> Tag | TagGetError:
        # FIXME this doesn't work
        tag = self.get_by_id(id)

        if type(tag) is TagGetError:
            return tag
        
        if tag.user_id != user_id:
            return TagGetError.NO_PERMISSION

        return tag

    def create_new(self, tag: Tag) -> Tag | TagCreateError:
        # FIXME this doesn't seem to work
        try:
            with self.conn.cursor(row_factory=class_row(Tag)) as cur:
                tag = cur.execute(
                    "INSERT INTO tags (user_id, name) VALUES (%s, %s) RETURNING id, user_id, name",
                    (tag.user_id, tag.name),
                ).fetchone()

                if tag is None:
                    return TagCreateError.DATABASE_ERROR
                return tag
        except psycopg.Error:
            return TagGetError.DATABASE_ERROR

    def create_new_checked(self, tag: Tag, user_id: str) -> Tag | TagCreateError:
        if tag.user_id != user_id:
            return TagCreateError.NO_PERMISSION

        return self.create_new(tag)
