from datetime import datetime
from enum import Enum, auto
from pydantic import BaseModel


class Status(Enum):
    processing = auto()
    done = auto()


class Job(BaseModel):
    id: str
    object_id: str
    status: Status
    timestamp: datetime
