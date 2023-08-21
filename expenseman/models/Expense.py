from dataclasses import dataclass
from datetime import datetime
from .Tag import Tag


@dataclass
class DbExpense:
    id: str
    description: str
    expense_time: datetime
    user_id: str


@dataclass
class Expense(DbExpense):
    tags: list[Tag]
