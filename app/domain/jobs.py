from app.adapters import db, queues
from app.models import Job
from typing import Union
import datetime


def process(object_id: str) -> Job:
    """
    If the object_id is found in the db for the last 5 minutes,
    it retrieves this job's information and skips processing.
    If the object_id cannot be found in the db for the last 5 minutes,
    it saves it and sends it to a queue to be processed.
    :param object_id:
    :return: Job information
    """
    jobs = db.Jobs().get_by_object_id(object_id)
    job_processed_in_last_five_minutes = list(
        filter(
            lambda x: (
                datetime.datetime.utcnow() - x.timestamp < datetime.timedelta(minutes=5)
            ),
            jobs,
        )
    )
    if job_processed_in_last_five_minutes:
        return sorted(job_processed_in_last_five_minutes, key=lambda x: x.timestamp)[0]

    # todo: add error handling
    new_job = db.Jobs().create(object_id)
    publisher = queues.Publisher()
    publisher.publish(new_job.id)

    return new_job


def retrieve(received_job_id: str) -> Union[Job, None]:
    """
    It retrieves the job's information that finds in the db or None if the job was not found.
    :param received_job_id:
    :return:
    """
    # todo: add error handling
    found_job = db.Jobs().get_by_id(received_job_id)
    if not found_job:
        return
    return found_job


def finish(ch, method, properties, body) -> Union[Job, None]:
    """
    It retrieves the job from the job_id received in the 'body' parameter.
    Looks for it in the db and updates its status to 'done'.
    If no job was found, it returns None.
    :param ch:
    :param method:
    :param properties:
    :param body:
    :return:
    """
    del ch, method, properties
    # todo: add error handling
    found_job = db.Jobs().get_by_id(body)
    if not found_job:
        return
    found_job.status = "done"
    return db.Jobs().update(found_job)
