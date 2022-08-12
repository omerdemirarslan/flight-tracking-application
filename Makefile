### MakeFile


## Run The Project:

build:
	docker-compose build

up:
	docker-compose up

up-build:
	docker-compose up --build

run-test:
	docker-compose run --rm flight-tracking ./manage.py test
