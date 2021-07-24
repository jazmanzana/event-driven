# todo: remove from here
import sqlalchemy as sa


class Job:
    __tablename__ = "jobs"
    __table_args__ = (sa.PrimaryKeyConstraint("object_id", "id", name="jobs_pkey"),) # todo: rethink pkey
    id = sa.Column(sa.String(), nullable=False, primary_key=True)
    object_id = sa.Column(sa.String(), nullable=False, primary_key=True)
    status = sa.Column(sa.String(), nullable=False, primary_key=True)
    timestamp = sa.Column(sa.DateTime(timezone=False), nullable=False)
