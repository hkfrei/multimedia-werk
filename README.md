# Karten-Werk Website

The new Django Karten-Werk website.

## Getting started locally

First get a copy of the app

```
git clone https://github.com/hkfrei/karten-werk-django.git
cd karten-werk-django
```

### Start the development environment

Create virtual python environment:

```
pip install virtualenv
virtualenv --python C:\path_to_python\python3.9.exe env
```

...and activate it

```
.\env\Scripts\activate
```

### install requirements

```
pip install -r ./requirements.txt
```

### Then we have to create an .env file, holding our environment variables

```
cd website
touch .env
```

The following variables need to be defined:

- DB_NAME="name of the database to store models etc."
- DB_USER="database username"
- DB_PASSWORD="database password"
- DB_HOST="database host"
- DB_PORT="database port"
- DB_TIME_ZONE="the time-zone of the database"

### Start the server

- make sure you are in the _geourbackend_ folder (the one which has the _manage.py_ file)
- from there call `python manage.py runserver` from within you console.
- open (http://localhost:8000/)[http://localhost:8000/] to see the site running.
