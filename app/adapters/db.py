from app.models import Job
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


class Jobs:
    def __init__(self):
        Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        self.session = Session()

    def get_by_id(self, job_id: str):
        try:
            return self.session.query(Job).filter(Job.id == job_id).first()
        except sa.orm.exc.NoResultFound:
            raise errors.NoResultFound()

    def get_by_object_id(self, object_id: str):
        try:
           return self.session.query(Job).filter(Job.object_id == object_id).all()  # todo: filter vs filter_by?
        except sa.orm.exc.NoResultFound:
           raise errors.NoResultFound()

    def create_or_update(self, object_id) -> Job:
        job = Job(object_id=object_id)
        self.session.add(job)
        self.session.commit()
        self.session.refresh(job)
        return job
