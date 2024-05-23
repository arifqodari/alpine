import logging

from alpine.settings import gunicorn_settings


workers = gunicorn_settings.gunicorn_num_workers
threads = gunicorn_settings.gunicorn_num_threads
timeout = gunicorn_settings.gunicorn_timeout
worker_class = "uvicorn.workers.UvicornWorker"
bind = '0.0.0.0:80'
accesslog = "-"


def filter_health_check_log(record):
    return record.args[2] != "/health"


def post_worker_init(worker):
    access_logger = logging.getLogger("uvicorn.access")
    access_handler = access_logger.handlers[0]
    new_formatter = logging.Formatter(
        fmt="%(asctime)s [%(process)d] [%(levelname)s] %(message)s",
        datefmt="[%Y-%m-%d %H:%M:%S %z]"
    )
    access_handler.setFormatter(new_formatter)
    access_logger.addFilter(filter_health_check_log)
