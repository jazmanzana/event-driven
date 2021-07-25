from typing import Dict, Any
from app.adapters import db
import datetime


# todo https://stackoverflow.com/questions/51291722/define-a-jsonable-type-using-mypy-pep-526
def process(object_id: str) -> Dict[str, Any]:
    jobs = db.Jobs().get_by_object_id(object_id)
    print(f"Jobs returned by db: {jobs}")

    job_processed_in_last_five_minutes = list(filter(lambda x: (datetime.datetime.now() - x["timestamp"] < datetime.timedelta(minutes=5)), jobs))
    print(f"job_processed_in_last_five_minutes: {job_processed_in_last_five_minutes}")
    if job_processed_in_last_five_minutes:
        # todo: this should be serialized before returning
        # todo: we need to return more info
        old_job = sorted(job_processed_in_last_five_minutes, key=lambda x: x["timestamp"])[0]
        return {"job_id": f"{old_job.id}"}

    # todo: if db or enqueuing fail, returns error to user
    #queues.enqueue(object_id)
    print("ENQUEUING SIMULATOR!!!")
    new_job = db.Jobs().create_or_update(object_id)

    return {"job_id": f"{new_job.id}"}


def get_by_id(received_job_id: str) -> Dict[str, Any]:
    print(f"Received job id: {received_job_id}")
    found_job = db.Jobs().get_by_id(received_job_id)
    if found_job:
        # todo: we need to return more info
        return {"job_id": f"{found_job.id}"}
    else:
        return {"message": f"job with id '{received_job_id}' not found"}