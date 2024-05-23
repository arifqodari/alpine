.PHONY: check clean install run_debug run


clean:
	find . | grep -E "(__pycache__|\.pyc|\.lprof)" | xargs rm -rf

install: clean
	pip freeze | grep -v -f requirements.txt - | xargs pip uninstall -y
	pip install -r requirements.txt

dev:
	fastapi dev alpine/api

run:
	gunicorn -c alpine/gunicorn_config.py alpine.api:app -b :8000