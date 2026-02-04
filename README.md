
```md
# Python + FastAPI + MySQL (Dockerized)

This project is an intermediate-level backend application built using **Python**, **FastAPI**, and **MySQL**, fully containerized with **Docker** and **Docker Compose**.

The main goal of this project is to practice:
- Understanding an unfamiliar Python backend repository
- Identifying the application entry point
- Writing Dockerfiles correctly
- Connecting an application container to a database container

---

## Project Structure

```

python-fastapi-mysql/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
├── README.md
└── app/
├── main.py
├── db.py
└── routes/
└── users.py

```

---

## Tech Stack

- Python 3.11
- FastAPI
- Uvicorn
- MySQL 8
- Docker
- Docker Compose

---

## Application Flow

1. Application starts using **Uvicorn**
2. Entry point: `app/main.py`
3. FastAPI app is initialized
4. Routes are registered from `routes/users.py`
5. Database connection is handled in `db.py`
6. MySQL runs as a separate container

---

## Environment Variables

Create a `.env` file in the project root:

```

DB_HOST=db
DB_USER=root
DB_PASSWORD=root
DB_NAME=appdb

````

> Note: `DB_HOST` must be set to `db`, which is the Docker Compose service name.

---

## Running the Application

### Using Docker Compose

Build and start the application and database:

```bash
docker-compose up --build
````

---

## API Endpoints

| Endpoint | Description                  |
| -------- | ---------------------------- |
| `/`      | Health check                 |
| `/users` | Returns current DB timestamp |

---

## Accessing in Killercoda

1. Run `docker-compose up`
2. Expose port **8000** from Killercoda UI
3. Use the generated public URL:

```
https://<generated-url>/users
```

---

## Common Issues

### Cannot connect to MySQL

* Ensure `DB_HOST=db`
* Ensure MySQL container is running
* Check logs using:

```bash
docker logs <container_name>
```

---

## Useful Commands

```bash
docker-compose up
docker-compose up --build
docker-compose down
docker ps
docker logs
```

---

## Key Learnings

* Dockerfile must be placed at project root
* Service names act as DNS hostnames in Docker Compose
* Databases should always run in separate containers
* Application entry point differs by language, but Docker logic stays the same

---
