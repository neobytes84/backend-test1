# Microservicios Authors & Books – Prueba Técnica

Este proyecto implementa dos microservicios independientes que permiten:

Gestión de autores

# Gestión de libros

- Relación autor-libro mediante eventos Kafka

- Persistencia en PostgreSQL

- APIs REST con FastAPI

## Tecnologías Utilizadas

- Python 3.11

- FastAPI

- Uvicorn

- SQLAlchemy

- PostgreSQL

- Kafka + Zookeeper

- Docker & Docker Compose

## Levantar el Proyecto

Desde la raíz del repositorio:

docker compose up -d --build


## Servicios expuestos:

Servicio	Puerto
- authors-ms	8009
- books-ms	  8010
- authors-db	5433
- books-db	  5434
- kafka	      9092

## Swagger

- Authors-MS: http://localhost:8009/docs

- Books-MS: http://localhost:8010/docs

## Endpoints Principales
- Authors-MS

POST /authors/

GET /authors/

POST /authors/{author_id}/books/{book_id} → asignar autor a libro

- Books-MS

POST /books/

GET /books/

GET /books/{id}

## Flujo de Eventos (Kafka)

Authors-MS produce un evento cuando se asigna un autor a un libro.

Books-MS consume el evento y actualiza la relación en su base de datos.

## Tests

Ejecutar tests dentro de cada microservicio:

pytest



