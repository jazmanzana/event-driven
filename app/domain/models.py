from datetime import datetime
from enum import Enum, auto


class Status(Enum):
    processing = auto()
    done = auto()


class Job:
    id: str
    object_id: str
    status: Status
    timestamp: datetime

