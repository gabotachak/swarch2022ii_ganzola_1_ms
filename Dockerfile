# syntax=docker/dockerfile:1

FROM python:3.9-alpine

WORKDIR /swarch2022ii_1_ms

ENV DB_HOST host.docker.internal
ENV DB_PORT 3306
ENV DB_SCHEMA swarch2022ii_1_db
ENV DB_USER root
ENV DB_PASSWORD password

COPY requirements.txt requirements.txt
RUN apk add build-base
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]

EXPOSE 5000
