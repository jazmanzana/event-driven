from typing import Optional
from fastapi import FastAPI, Body

app = FastAPI()
# check Collections

@app.get("/")
def home():
    return {'hola': 'perrrruuuuuuu'}

@app.get("/jobs/{id}")
def get_job(id: str):
    return {"message": f"Llegaste aca y me tiraste el id: {id}"}

@app.post("/jobs/process")
def create_job(id: str = Body(...)):
    # tiene que recibir object id
    return {"message": f"Llegaste aca y me tiraste el id: {id}"}

