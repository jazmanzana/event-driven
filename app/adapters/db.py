from app.models import Job
from typing import List
import sqlalchemy as sa
from app import errors
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database


# todo: remove connection string from here
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@db/db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
if not database_exists(engine.url):
    create_database(engine.url)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Jobs:
    def __init__(self):
        self.session = Session()

    def get_by_id(self, job_id: str) -> Job:
        try:
            return self.session.query(Job).filter(Job.id == job_id).one()
        except sa.orm.exc.NoResultFound:
            raise errors.NoResultFound()

    def get_by_object_id(self, object_id: str) -> List[Job]:
        try:
           return self.session.query(Job).filter(Job.object_id == object_id).all()  # todo: filter vs filter_by?
        except sa.orm.exc.NoResultFound:
           raise errors.NoResultFound()

    def create(self, object_id) -> Job:
        job = Job(object_id=object_id)
        self.session.add(job)
        self.session.commit()
        self.session.refresh(job)
        return job

    def update(self, updated_job: Job) -> Job:
        to_update_job = self.session.query(Job).filter(Job.id == updated_job.id).one()
        to_update_job.status = updated_job.status
        self.session.commit()
        return to_update_job
