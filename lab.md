# Laboratorio práctico

## Autor: Gabriel Andres Anzola Tachak

## i. Introducción

Como ejemplo práctico de la asignatura, se creará un sistema de software distribuido, este ejemplo consiste en una aplicación que lleva registro de transacciones financieras.

- Tipo de componente: Microservicio
- Nombre del componente: swarch2022ii_1_ms
- Lenguaje de programación: Python
- Framework: Flask
- Puerto: 5000

## ii. Requisitos

- Base de datos desplegada: [base de datos](https://github.com/ganzola/swarch2022ii_ganzola_1_db)

- Endpoints para insomnia: [descargar insomnia](https://insomnia.rest/)

## iii. Componente: Microservicio

- Puerto TCP a usar: 5000.

### a. Código Fuente

El código fuente se encuentra en el siguente enlace: [micorservicio](https://github.com/ganzola/swarch2022ii_ganzola_1_ms)

### b. Arquitectura Interna del Microservicio

La arquitectura interna (sub-arquitectura) del microservicio está compuesta por los siguientes tres elementos:

- Models: abstracción del modelo de datos.
- Views: gestión de peticiones HTTP basada en el estilo arquitectónico REST.
- Controllers: lógica de negocio y gestión de datos.

### c. Dockerización

En la raíz del proyecto se encuentra un archivo llamado Dockerfile:

```docker
# syntax=docker/dockerfile:1

FROM python:3.9-alpine

WORKDIR /swarch2022ii_1_ms

ENV DB_HOST host.docker.internal
ENV DB_PORT 3000
ENV DB_SCHEMA swarch2022ii_1_db
ENV DB_USER root
ENV DB_PASSWORD password

COPY requirements.txt requirements.txt
RUN apk add build-base
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]

EXPOSE 5000
```

Allí se encuentra la información necesaria para la instalación de dependencias y las credenciales de la base de datos.

### d. Creacíon de imagen y despliegue del contenedor

```console
docker build --tag swarch2022ii_1_ms .
docker run --name swarch2022ii_1_ms -d -p 4000:5000 swarch2022ii_1_ms
```

## iii Endpoints:

[endpoints](endpoints.json)
