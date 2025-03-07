from dataclasses import dataclass
from datetime import datetime


@dataclass
class Task:
    id: int
    title: str
    completed: bool
    created_at: datetime
