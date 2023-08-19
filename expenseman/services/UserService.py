from abc import ABC, abstractmethod
from ..models import User
from enum import Enum


class UserCreateError(Enum):
    DATABASE_ERROR = 1
    EMAIL_ALREADY_EXISTS = 2
    PASSWORD_TOO_SHORT = 3
    UNKNOWN_ERROR = 4


class UserGetError(Enum):
    DATABASE_ERROR = 1
    USER_DOES_NOT_EXIST = 2

class LoginError(Enum):
    DATABASE_ERROR = 1
    USER_DOES_NOT_EXIST = 2
    INVALID_PASSWORD = 3

class UserService(ABC):
    @abstractmethod
    def get_all(self) -> list[User] | UserGetError:
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> User | UserGetError:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> User | UserGetError:
        pass

    @abstractmethod
    def create_new(self, user: User) -> User | UserCreateError:
        pass

    @abstractmethod
    def login(self, user: User) -> str | LoginError:
        pass
