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
        old_job = sorted(job_processed_in_last_five_minutes, key=lambda x: x["timestamp"])[0]
        return {"job_id": f"{old_job.id}"}

    # todo: if db or enqueuing fail, returns error to user
    #queues.enqueue(object_id)
    print("ENQUEUING SIMULATOR!!!")
    new_job = db.Jobs().create_or_update(object_id)

    return {"job_id": f"{new_job.id}"}


def get_by_id(job_id: str) -> Dict[str, Any]:
    print(f"Received job id: {job_id}")
    # todo: query db
    return {"job_id": f"{job_id}"}
