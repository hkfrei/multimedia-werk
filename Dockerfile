FROM python:3.9.10-alpine

# working directory
WORKDIR /app
# environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PORT 8000

# install requirements
COPY requirements.txt requirements.txt
# install linux packages in order to be able to install all the python requirements
RUN apk update && apk add \
postgresql-dev gcc python3-dev libc-dev tk-dev linux-headers musl-dev 
# install the requirements
RUN pip install -U pip && pip install -r requirements.txt

# copy everything to the app folder.
COPY . .

# make scripts executable
RUN chmod +x /app/entrypoint.sh
# Installing uwsgi server.
RUN pip install uwsgi

CMD ["/app/entrypoint.sh"]
