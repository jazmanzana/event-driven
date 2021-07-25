from typing import Dict, Any
from fastapi import FastAPI
from app.domain import jobs
from app.adapters import db
from pydantic import BaseModel
from app import models

models.Base.metadata.create_all(bind=db.engine)
app = FastAPI()


class ObjectBody(BaseModel):
    id: str

# opcion 1: leo de las cola DONE cuando tengo un get
# opcion 2: somehow el exchange me llama por http o rpc
# opcion 3: leo la cola cada t tiempo: cron job?
# opcion 4: el worker me llama cuando termina


@app.get("/jobs/{job_id}")
def get_job(job_id: str) -> Dict[str, Any]:
    # todo: validate job_id is uuid
    # todo: add error handling
    return jobs.retrieve(job_id)


@app.post("/jobs/process")
def create_job(body: ObjectBody) -> Dict[str, Any]:
    # todo: add error handling
    return jobs.process(body.id)
