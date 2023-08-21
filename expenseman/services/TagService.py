from abc import ABC, abstractmethod
from ..models import Tag
from enum import Enum


class TagGetError(Enum):
    """Error enum for tag fetching"""

    DATABASE_ERROR = 1
    TAG_DOES_NOT_EXIST = 2
    NO_PERMISSION = 3


class TagCreateError(Enum):
    DATABASE_ERROR = 1
    NO_PERMISSION = 2


class TagService(ABC):
    """Abstract class to fetch/create tags"""

    @abstractmethod
    def get_all(self) -> list[Tag] | TagGetError:
        pass

    @abstractmethod
    def get_all_by_user(self, user_id: str) -> list[Tag] | TagGetError:
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> Tag | TagGetError:
        pass

    @abstractmethod
    def get_by_id_checked(self, id: str, user_id: str) -> Tag | TagGetError:
        pass

    @abstractmethod
    def create_new(self, tag: Tag) -> Tag | TagCreateError:
        pass

    @abstractmethod
    def create_new_checked(self, tag: Tag, user_id: str) -> Tag | TagCreateError:
        pass
