from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sa
import datetime
from enum import Enum, auto
import uuid

Base = declarative_base()


class Status(Enum):
    processing = "processing"
    done = "done"


class Job(Base):
    __tablename__ = "jobs"
    __table_args__ = (sa.PrimaryKeyConstraint("id", name="jobs_pkey"),)
    id = sa.Column(
        UUID(as_uuid=True), nullable=False, primary_key=True, default=uuid.uuid4
    )
    object_id = sa.Column(sa.String(), nullable=False)
    status = sa.Column(sa.types.Enum(Status), nullable=False, default=Status.processing)
    timestamp = sa.Column(
        sa.DateTime(timezone=False), nullable=False, default=datetime.datetime.utcnow
    )
