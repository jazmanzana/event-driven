FROM python:3.8

COPY . ./worker

RUN pip install --upgrade pip

RUN pip install -r /worker/requirements.txt

CMD ["uvicorn", "worker.main:app", "--host", "0.0.0.0", "--port", "5000"]