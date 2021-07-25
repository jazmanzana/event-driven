FROM python:3.8

COPY . ./processor_worker

RUN pip install --upgrade pip

RUN pip install -r /worker/requirements.txt

# improve this
CMD ["python", "main.py"]