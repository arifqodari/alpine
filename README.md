Alpine - FastAPI Template
===


Clone and get running.

## Configuration

```sh

# whether the app is in debug mode or not
# debug mode will output a lot more logs
IS_DEBUG

# number of gunicorn worker to handle multiple requests
GUNICORN_NUM_WORKERS

# number of gunicorn threads
GUNICORN_NUM_THREADS

# timeout in seconds of gunicorn to handle a single request
GUNICORN_TIMEOUT
```


## Installation

```sh
pip install -r requirements.txt
```


## Develop

To run the API in dev environment, run the following command

```sh
make dev
```


## Run Gunicorn

Set up environment variables needed before running the gunicorn server.
Then, run the following command:

```sh
make run
```