from fastapi import FastAPI
from domain import job_processor
from pydantic import BaseModel

app = FastAPI()
# todo check Collections


@app.post("/jobs/process")
def create_job():
    job_processor.process()
    return {"message": f"Your job is being processed."}

