from typing import Optional
from fastapi import FastAPI

app = FastAPI()
# check Collections

@app.get("/")
def home():
    return {}

@app.get("/jobs/{id}")
def create_job(id: str):
    return {"message": "Llegaste aca."}

@app.post("/jobs/process")
def create_job():
    # tiene que recibir object id
    return {"message": "Llegaste aca."}

