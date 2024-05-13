# Flask boilerplate

Purpose of this repo:
Create a boilerplate for a scalable but still compact Flask app.

You can run the app using either Docker or pipenv

The only thing missing here to run the app is set of secrets. You can mock CONFIG_TYPE = config.DevConfig, SOME_SECRET, TEST_DB_SECRET, PROD_DB_SECRET, DEV_DB_SECRET in .env file

This is still work in progress, however, the main idea is laid out in the existing code.


#### To Setup and Start
```bash
pipenv shell
pipenv install
pipenv flask --debug run
```
or 
```bash
docker build -t flask-tribe .


```
## Endpoints

#### Get All Request Records
```bash
curl -X GET http://127.0.0.1:5000/book_requests
```

#### Get One Request Record
```bash
curl -X GET http://127.0.0.1:5000/book_request/8c36e86c-13b9-4102-a44f-646015dfd981
```

#### Add A New Record
```bash
curl -X POST http://127.0.0.1:5000/book_request -H 'Content-Type: application/json' -d '{"title":"Booksy Book", "email": "testuser3@test.com"}'
```

#### Edit An Existing Record
```bash
curl -X PUT http://127.0.0.1:5000/book_request -H 'Content-Type: application/json' -d '{"title":"edited Booksy Book", "email": "testuser4@test.com"}'
```

#### Delete A Record
```bash
curl -X DELETE http://127.0.0.1:5000/book_request/04cfc704-acb2-40af-a8d3-4611fab54ada
```
## Testing
This project is using pytest. While running your enviroment run  ```python -m pytest``` 

## Structure
```
|__app
|  |__ blueprints (flask routes grouped by their domain)
|  |__ __init__.py (main flask file that is calling to all other files)
|
|__tests 
|    |__ endpoints (test of flask endpoints)
|    |__ integration (test of 3rd party integrations with this app (empty so far))
|    |__ unit (smallest use cases test)
|    |__ conftest.py (pytest configuration file, contains a setup that can be reused in all tests)
|
|
|__config.py (flask-wide configuration file, so we can use different set e.g. env variables for each environmet)
|
|__Dockerfile (configuration for running this app with Docker)
|
|__main.py (this flask app "entry point", depending on cloud plafform deployment choice, you might have to rename it)
|
|__Pipfile (pipenv config, needed when using pipenv to run this project)
|
|__Pipfile.lock (pipenv config)
|
|__requirements.txt (config file needed for running this app when NOT using pipenv, but generated using "pipenv run pip freeze  > requirements.txt")

```

