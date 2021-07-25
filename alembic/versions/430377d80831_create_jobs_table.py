"""create jobs table

Revision ID: 430377d80831
Revises: 
Create Date: 2021-07-25 09:06:37.528816

"""
from sqlalchemy.dialects.postgresql import UUID
from alembic import op
import sqlalchemy as sa
import datetime
import enum
import uuid


# revision identifiers, used by Alembic.
revision = "430377d80831"
down_revision = None
branch_labels = None
depends_on = None


class Status(enum.Enum):
    processing = "processing"
    done = "done"


def upgrade():
    op.create_table(
        "jobs",
        sa.Column(
            "id",
            UUID(as_uuid=True),
            nullable=False,
            primary_key=True,
            default=uuid.uuid4,
        ),
        sa.Column("object_id", sa.String(), nullable=False, primary_key=True),
        sa.Column(
            "status", sa.types.Enum(Status), nullable=False, default=Status.processing
        ),
        sa.Column(
            "timestamp",
            sa.DateTime(timezone=False),
            nullable=False,
            default=datetime.datetime.utcnow,
        ),
    )


def downgrade():
    op.drop_table("jobs")
