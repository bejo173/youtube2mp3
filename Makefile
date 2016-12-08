SHELL:=/bin/bash

init:
	virtualenv --python=python3 venv && source ./venv/bin/activate && pip install -r requirements.txt && deactivate

# Run in Development environment
run-in-dev:
	source ./venv/bin/activate && export APP_CONFIG=config.DevelopmentConfig; python youtube2mp3/app.py

# Run in Production environment
run-in-prod:
	source ./venv/bin/activate && export APP_CONFIG=config.ProductionConfig; python youtube2mp3/app.py

.PHONY: test
test:
	nosetests -v ./test