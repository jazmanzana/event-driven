FROM python:3.8

COPY . ./worker

RUN pip install --upgrade pip

RUN pip install -r /worker/requirements.txt

CMD ["python", "-m", "worker.main"]