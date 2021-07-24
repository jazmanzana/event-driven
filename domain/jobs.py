import time
from typing import Dict, Any
from adapters.db import db


# todo https://stackoverflow.com/questions/51291722/define-a-jsonable-type-using-mypy-pep-526
def process(object_id: str) -> Dict[str, Any]:
    print(f'About to process object id: {object_id}')
    jobs = db.Jobs().get_by_object_id(object_id)
    # todo 0 - si tengo resultados en los ultimos 5 minutos, devuelvo el job id que me devuelve la db
    # todo 1 - si no tengo resultados en los ultimos 5 minutos:
    # todo 1.1 - mando job a la cola
    # todo 1.2 - escribo entry en la tabla
    # todo 1.3 - devuelvo job id
    print('these jobs were found: ', jobs)
    time.sleep(15)
    return {"job_id": "made-up-job-id"}