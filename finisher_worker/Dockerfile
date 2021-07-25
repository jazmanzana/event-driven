FROM python:3.8

COPY . ./finisher_worker

RUN pip install --upgrade pip

RUN pip install -r /finisher_worker/requirements.txt

# improve this
CMD ["python", "main.py"]