# Karten-Werk Website

The Multimedia-Werk website.

## Getting started locally

First get a copy of the app

```
git clone https://github.com/hkfrei/multimedia-werk.git
cd multimedia-werk
```

### Start the development environment

Create virtual python environment:
You can get the path to your python executable with this commands:

```
python3
>>> import os
>>> import sys
>>> os.path.dirname(sys.executable)

/opt/homebrew/opt/python@3.10/bin

```

```
pip3 install virtualenv
virtualenv --python /opt/homebrew/opt/python@3.10/bin/python3.10 env

```

...and activate it

```
source env/bin/activate

```

### install requirements

```
pip install -r ./requirements.txt
```

### Then we have to create an .env file, holding our environment variables

```
touch .env
```

The following variables need to be defined:

- DB_NAME="name of the database to store models etc."
- DB_USER="database username"
- DB_PASSWORD="database password"
- DB_HOST="database host"
- DB_PORT="database port"
- DB_TIME_ZONE="the time-zone of the database"
- SECRET_KEY="Django secret key"
- GOOGLE_MAPS_API_KEY="API Key for google maps"
- EMAIL_HOST = "email hostname"
- EMAIL_PORT = "email port number"
- EMAIL_HOST_USER = "username for the host"
- EMAIL_HOST_PASSWORD = "email password"

### Start the server

- make sure you are in the _multimedia-werk_ folder (the one which has the _manage.py_ file)
- from there call `python manage.py runserver` from within you console.
- open (http://localhost:8000/)[http://localhost:8000/] to see the site running.

### Deploy to Google Cloud Run

1. Create a Docker Image and save in the Google Cloud:

   ```
   gcloud builds submit --tag europe-west6-docker.pkg.dev/multimediawerk/multimediawerk-website/docker.latest
   ```

2. Deploy to Cloud Run
   ```
   gcloud run deploy multimedia-werk-website --platform managed --region europe-west6 --image europe-west6-docker.pkg.dev/multimediawerk/multimediawerk-website/docker.latest:latest --set-secrets "DB_HOST=DB_HOST:latest,DB_PORT=DB_PORT:latest,DB_PASSWORD=DB_PASSWORD:latest,DB_NAME=DB_NAME:latest,DB_USER=DB_USER:latest,DB_PASSWORD=DB_PASSWORD:latest,SECRET_KEY=SECRET_KEY:latest, DB_TIME_ZONE=DB_TIME_ZONE:latest, GOOGLE_MAPS_API_KEY=GOOGLE_MAPS_API_KEY:latest, EMAIL_HOST=EMAIL_HOST:latest, EMAIL_PORT=EMAIL_PORT:latest, EMAIL_HOST_USER=EMAIL_HOST_USER:latest, EMAIL_HOST_PASSWORD=EMAIL_HOST_PASSWORD:latest" --service-account cloudrun-serviceaccount@multimediawerk.iam.gserviceaccount.com --allow-unauthenticated --max-instances=10 --memory=256Mi
   ```

Open: https://multimedia-werk-website-2xbrpq5qzq-oa.a.run.app/
