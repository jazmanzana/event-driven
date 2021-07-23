FROM python:3.8

COPY . .

RUN pip install --upgrade pip
RUN pip install poetry

RUN pip install -r requirements.txt

#ENTRYPOINT ["/bin/project"]
CMD ["uvicorn", "main:app", "--reload"]
#"python", "-m",