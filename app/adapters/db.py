from app.models import Job
from typing import List, Union
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sqlalchemy as sa
from sqlalchemy_utils import database_exists, create_database
import os


SQLALCHEMY_DATABASE_URL = f"{os.getenv('DB_DRIVER')}://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_URL')}/{os.getenv('DB_NAME')}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
if not database_exists(engine.url):
    create_database(engine.url)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Jobs:
    def __init__(self):
        self.session = Session()

    def get_by_id(self, job_id: str) -> Union[Job, None]:
        try:
            job_id = job_id.decode("utf-8")
        except AttributeError:
            pass
        try:
            return self.session.query(Job).filter(Job.id == job_id).one()
        except sa.orm.exc.NoResultFound:
            return None

    def get_by_object_id(self, object_id: str) -> List[Job]:
        try:
            return self.session.query(Job).filter(Job.object_id == object_id).all()
        except sa.orm.exc.NoResultFound:
            return []

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
