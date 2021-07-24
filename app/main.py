#from typing import Optional
from fastapi import FastAPI
from domain import jobs
from pydantic import BaseModel

app = FastAPI()
# check Collections


class ObjectBody(BaseModel):
    id: str


@app.get("/")
def home():
    return {'hola': 'perrrruuuuuuu'}


@app.get("/jobs/{job_id}")
def get_job(job_id: str):
    return {"message": f"Llegaste aca y me tiraste el id: {job_id}"}


@app.post("/jobs/process")
def create_job(body: ObjectBody):
    print(f'Received body: {body}')
    job_id = jobs.process(body.id)  # todo: try catch statement
    return {"message": f"Your job with id '{job_id}' is being processed."}

