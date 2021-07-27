# event-driven

### Setting it up
1. Clone the repository:
    ```
    git clone git@github.com:jazmanzana/event-driven.git
    ```
2. Enter the folder:

    ```
    cd event-driven
    ```
3. Create the following .env files:
 - `app/.env` containing 
   - DB_USERNAME=postgres
   - DB_PASSWORD=postgres
   - DB_DRIVER=postgresql
   - DB_URL=db
   - DB_NAME=db
 - in the root of the repository, a `.env` file containing:
   - POSTGRES_PASSWORD=postgres
   - JOB_EXPIRATION=60000 (in miliseconds)


###  How to run locally
1. Run the command to create the infrastructure:
```
make run-infra
```

2. Once db and queues finish initializting, run:

```
make run-app
```

Which will initialize the app (who will be listening on `0.0.0.0:8000`) and the worker.


### How to test

```
make test
```

### Available endpoints
`GET /jobs/{job_id}`
   
Description: Returns all the information related to that job.


`POST /jobs`  
Body must contain the key `object_id`. Body example:
 `{'object_id': 'example-object-id'}` 

Description: Creates a job resource and starts processing it. It returns the created job information.


