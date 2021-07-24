from typing import Dict, Any
import datetime


# todo https://stackoverflow.com/questions/51291722/define-a-jsonable-type-using-mypy-pep-526
def process(object_id: str) -> Dict[str, Any]:
    print(f'About to process object id: {object_id}')
    # jobs = db.Jobs().get_by_object_id(object_id)  # todo: voy a intentar hacerlo andar luego
    jobs = [{"id": "job_0", "object_id": "object_id_0", "status": "processing", "timestamp": datetime.datetime(2021, 7, 24, 15, 0, 0, 0)}]
    job_processed_in_last_five_minutes = list(filter(lambda x: (datetime.datetime.now() - x["timestamp"] < datetime.timedelta(minutes=5), jobs)))
    if job_processed_in_last_five_minutes:
        return job_processed_in_last_five_minutes[0]  # todo: order by timestamp before returning?
    # todo 1.1 - mando job a la cola
    # todo 1.2 - escribo entry en la tabla
    return {"job_id": "made-up-job-id"}