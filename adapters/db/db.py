from models import Job
import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import errors


class Jobs:
    def __init__(self):
        # todo: remove connection string from here
        engine = create_engine('postgresql://jaz:zaj@localhost:5432/jobs', echo=True)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def get_by_id(self, job_id: str):
        pass

    def get_by_object_id(self, object_id: str):
        print(f"about to get_by_object_id with object id '{object_id}'")
        print(f"session is: '{self.session}' and its dir results in '{dir(self.session)}'")
        print(f"Job is: '{Job}' and its dir results in '{dir(Job)}'")
        try:
           query = self.session.query(Job).filter_by(Job.object_id == object_id)  # todo: filter vs filter_by?
           print(f"query to be executed: {query}")
           return query.all()
        except sa.orm.exc.NoResultFound:
           raise errors.NoResultFound()

    def create_or_update(self):
        pass
