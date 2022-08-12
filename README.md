# flight-tracking-application

---

## Requirements
* Python = 3.9
* PostgreSQL Database = 13
* [Docker](https://www.docker.com/)
* .env file on the project main line
* Install Makefile plugin: **If you want to run project makefile command**
---

## Description

This project main name:
* flight_tracking_application

This project has one app.
* flight_tracking


This project was created to manage all the record flights that our company processes. These processes:

* New Airport Information Create.
* Current Airport Information Update.
* Current Airport information delete.
* Current All Airport Information Listing.

* New Flight Information Create.
* Current Flight Information Update.
* Current Flight information delete.
* Current All Flight Information Listing.


We are use pre-commit on this project. You have to set pre-commit for before controls committed:
* pre-commit install
---

## Installation
    git clone https://github.com/omerdemirarslan/flight-tracking-application.git
---

## Run The Project:

### Docker way:

#### Example .env file content:

* POSTGRES_DB=flight_tracking_app
* POSTGRES_HOST=postgres
* POSTGRES_USER=captain
* POSTGRES_PASSWORD=007007
* POSTGRES_PORT=5432


#### Command Steps

```shell
$ docker-compose build
$ docker-compose up
```

#### Single Command

```shell
$ docker-compose up  --build
```


#### Move To Home Page

```shell
$ http://localhost:8000/
```


#### Move To Test API With Swagger Interface

```shell
$ http://0.0.0.0:8000/api/v1/docs/
```

#### Test Project

```shell
$ docker-compose run --rm flight-tracking ./manage.py test --pattern="test_*.py"
```
---

```text
You can add the database source in your IDE database management or other database interface.

The credentials for database in the docker:
Host: 0.0.0.0 # Because project runs ıt host on your local.
Port: 6432 # Because Docker use 5432 default port in base postgresql but It need difference port local project.
Database: flight_tracking_app
User: captain
Password: 007007
```

### Local Environment Way

#### Create database in your local device. Like: **flight_tracking_app**

* For command line check this: [Postgresql](https://www.postgresql.org/docs/13/tutorial-createdb.html)
* The other way is PgAdmin Interface. Check this:
[PgAdmin](https://www.postgresqltutorial.com/postgresql-administration/postgresql-create-database/)

#### Example .env file content:

* POSTGRES_DB=flight_tracking_app
* POSTGRES_HOST=localhost
* POSTGRES_USER=postgres # General default username.
* POSTGRES_PASSWORD= "your password"
* POSTGRES_PORT=5432 # Local default port.


#### Create virtual environment & activate it
```shell
$ python3.9 -m venv flight_tracking_app
$ source flight_tracking_app/bin/activate
```

#### Install the requirements

```shell
$ pip install -r requirements.txt
```

#### Create Your Models

```shell
$ python manage.py migrate
```

#### Run project

```shell
$ python manage.py runserver 0.0.0.0:8000
```

#### Move To Home Page

```shell
$ http://localhost:8000/
```

#### Move To Test API With Swagger Interface

```shell
$ http://0.0.0.0:8000/api/v1/docs/
```

#### Test Project

```shell
python -m unittest
```
---
