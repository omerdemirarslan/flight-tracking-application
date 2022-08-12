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

#### 1- Copy Example .env file content:

* POSTGRES_DB=flight_tracking_app
* POSTGRES_HOST=postgres
* POSTGRES_USER=captain
* POSTGRES_PASSWORD=007007
* POSTGRES_PORT=5432


#### 2- Command Steps

```shell
$ docker-compose build
$ docker-compose up
```

#### 3- Single Command

```shell
$ docker-compose up  --build
```


#### 4- Visit To Home Page

```shell
$ http://localhost:8000/
```


#### 5- Visit To Test API With Swagger Interface

```shell
$ http://0.0.0.0:8000/api/v1/docs/
```

#### 6- Run All Test for Project

```shell
$ docker-compose run --rm flight-tracking ./manage.py test
```
---

#### 7- Add Data Source In the Database Management

```text
You can add the database source in your IDE database management or other database interface.

The credentials for database in the docker:
Host: 0.0.0.0 # Because project runs ıt host on your local.
Port: 6432 # Because Docker use 5432 default port in base postgresql but It need difference port local project.
Database: flight_tracking_app
User: captain
Password: 007007
```
---
