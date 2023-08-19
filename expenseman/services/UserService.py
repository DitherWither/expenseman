from abc import ABC, abstractmethod
from ..models import User
from enum import Enum


class UserCreateError(Enum):
    """Error enum when creation of user fails"""

    DATABASE_ERROR = 1
    EMAIL_ALREADY_EXISTS = 2
    PASSWORD_TOO_SHORT = 3
    UNKNOWN_ERROR = 4


class UserGetError(Enum):
    """Error enum for user fetching."""

    DATABASE_ERROR = 1
    USER_DOES_NOT_EXIST = 2


class LoginError(Enum):
    """Error enum for user creation."""

    DATABASE_ERROR = 1
    USER_DOES_NOT_EXIST = 2
    INVALID_PASSWORD = 3


class UserService(ABC):
    """Abstract Class to fetch data, and login/logout users."""

    @abstractmethod
    def get_all(self) -> list[User] | UserGetError:
        """Get all users as a list.

        :returns: list of users, or a UserGetError
        """
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> User | UserGetError:
        """Get user by id.

        :param id: uuid of the user to find
        :returns: User, or a UserGetError
        """
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> User | UserGetError:
        """Get user by email address.

        :param email: email address of the user to find
        :returns: User, or a UserGetError
        """
        pass

    @abstractmethod
    def create_new(self, user: User) -> User | UserCreateError:
        """Create a new user, and return it

        :param user: User to create. id field will be ignored
        :returns: The newly created user, or a UserCreateError
        """
        pass

    @abstractmethod
    def login(self, user: User) -> str | LoginError:
        """Log into a user

        :param user: User to log in as. id field will be ignored
        :returns: UUID of the user, or a LoginError
        """
        pass
