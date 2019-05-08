# Makefile

SHELL := /bin/bash

init:
	python3 -m venv venv; \
	source ./venv/bin/activate; \
	pip3 install --no-cache-dir -r requirements.txt; \

reinstall:
	source ./venv/bin/activate; \
	pip3 install --no-cache-dir -r requirements.txt; \

update_deps:
	source ./venv/bin/activate; \
	pip install --upgrade -r requirements.txt; \

run:
	./venv/bin/python3 manage.py runserver

revision:
	./venv/bin/alembic revision --autogenerate;

upgrade:
	./venv/bin/alembic upgrade head

downgrade:
	./venv/bin/alembic downgrade head

clear_pycache:
	py3clean .
