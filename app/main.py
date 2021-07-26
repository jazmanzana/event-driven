from typing import Dict
from fastapi import FastAPI, HTTPException
from app.domain import jobs
from app.models import Job
from app.adapters import db, queues
from pydantic import BaseModel
from app import models
from multiprocessing import Process


models.Base.metadata.create_all(bind=db.engine)
app = FastAPI()


def consume() -> None:
    """
    Initializes a consumer for a given queue and
    executes the set callback function with the body of the consumed message.
    :return:
    """
    consumer = queues.Consumer()
    consumer.set_callback(jobs.finish)
    consumer.start_consuming()


@app.on_event("startup")
def init_consumer() -> None:
    """
    Starts a separate process that consumes from a queue.
    :return:
    """
    p = Process(target=consume)
    p.start()


class ObjectBody(BaseModel):
    id: str


@app.get("/jobs/{job_id}")
def get_job(job_id: str) -> Dict[str, Job]:
    # todo: validate job_id is uuid
    # todo: add error handling
    job = jobs.retrieve(job_id)
    if not job:
        raise HTTPException(status_code=404, detail=f"Job '{job_id}' not found")
    return {"result": job}


@app.post("/jobs")
def create_job(body: ObjectBody) -> Dict[str, Job]:
    # todo: add error handling
    job = jobs.process(body.id)
    return {"result": job}
