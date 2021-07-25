from app.adapters import db, queues
from app.errors import NoResultFound
from app.models import Job
import datetime


# todo https://stackoverflow.com/questions/51291722/define-a-jsonable-type-using-mypy-pep-526
def process(object_id: str) -> Job:
    jobs = db.Jobs().get_by_object_id(object_id)
    job_processed_in_last_five_minutes = list(
        filter(
            lambda x: (
                datetime.datetime.now() - x.timestamp < datetime.timedelta(minutes=5)
            ),
            jobs,
        )
    )
    if job_processed_in_last_five_minutes:
        return sorted(job_processed_in_last_five_minutes, key=lambda x: x.timestamp)[0]

    # todo: add error handling
    new_job = db.Jobs().create(object_id)
    publisher = queues.Publisher().connect()
    publisher.publish(str(new_job.id))

    return new_job


def retrieve(received_job_id: str) -> Job:
    # todo: add error handling
    found_job = db.Jobs().get_by_id(received_job_id)
    if found_job:
        return found_job
    else:
        raise NoResultFound()


def finish(received_job_id: str) -> Job:
    # todo: add error handling
    found_job = db.Jobs().get_by_id(received_job_id)
    if not found_job:
        raise NoResultFound()
    found_job.status = "done"
    return db.Jobs().update(found_job)
