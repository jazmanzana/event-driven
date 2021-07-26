from typing import Dict
from fastapi import FastAPI
from app.domain import jobs
from app.models import Job
from app.adapters import db, queues
from pydantic import BaseModel
from app import models
from multiprocessing import Process


models.Base.metadata.create_all(bind=db.engine)
app = FastAPI()


def consume():
    consumer = queues.Consumer()
    consumer.set_callback(jobs.finish)
    consumer.start_consuming()


@app.on_event("startup")
def init_consumer():
    p = Process(target=consume)
    p.start()


class ObjectBody(BaseModel):
    id: str


@app.get("/jobs/{job_id}")
def get_job(job_id: str) -> Dict[str, Job]:
    # todo: validate job_id is uuid
    # todo: add error handling
    job = jobs.retrieve(job_id)
    return (
        {"result": job} if job else {"message": f"no job found for given id '{job_id}'"}
    )


@app.post("/jobs")
def create_job(body: ObjectBody) -> Dict[str, Job]:
    # todo: add error handling
    job = jobs.process(body.id)
    return {"result": job}


# app ha fallado con:
# sqlalchemy.exc.TimeoutError: QueuePool limit of size 5 overflow 10 reached, connection timed out, timeout 30.00 (Background on this error at: https://sqlalche.me/e/14/3o7r)
# worker fallaba con:
# pika.exceptions.ChannelClosedByBroker: (406, 'PRECONDITION_FAILED - delivery acknowledgement on channel 1 timed out. Timeout value used: 1800000 ms. This timeout value can be configured, see consumers doc guide to learn more')
