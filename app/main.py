from typing import Dict, Any
from fastapi import FastAPI
from app.domain import jobs
from app.domain import models as domain_models
from app.adapters import db
from pydantic import BaseModel
from app import models

models.Base.metadata.create_all(bind=db.engine)
app = FastAPI()


class ObjectBody(BaseModel):
    id: str


@app.get("/jobs/{job_id}")
def get_job(job_id: str) -> Dict[str, domain_models.Job]:
    # todo: validate job_id is uuid
    # todo: add error handling
    return {"result": domain_models.Job(**jobs.retrieve(job_id))}


@app.post("/jobs/process")
def create_job(body: ObjectBody) -> Dict[str, domain_models.Job]:
    # todo: add error handling
    return {"result": domain_models.Job(**jobs.process(body.id))}


@app.post("/jobs/finish")
def create_job(body: ObjectBody) -> Dict[str, domain_models.Job]:
    # todo: add error handling
    return {"result": domain_models.Job(**jobs.finish(body.id))}
