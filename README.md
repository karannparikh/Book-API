# Building a Containerized Book Management API

## Objective
Creating a RESTful API for managing a book database using Flask, SQLAlchemy, and MariaDB, then containerizing the application.

## Steps
1. Use Flask to create the API
2. Use SQLAlchemy as the ORM to interact with MariaDB
3. Implement CRUD operations for books
4. Containerize the application using Docker
5. Use docker-compose to manage the app and database containers

## API Endpoints
- `GET /api/name`: Get the API name
- `GET /books`: Retrieve all books
- `POST /books`: Create a new book
- `GET /books/<int:book_id>`: Retrieve a specific book by ID
- `PUT /books/<int:book_id>`: Update a specific book by ID
- `DELETE /books/<int:book_id>`: Delete a specific book by ID
- `POST /api/check-duplicate`: Check for duplicate books

## Running the Application
1. Build and run the Docker containers:
    ```sh
    docker-compose up --build
    ```
2. Access the API at `http://localhost:8080`

## Requirements
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-CORS
- pymysql

## Database Configuration
The application uses MariaDB as the database. The database configuration is specified in the `docker-compose.yml` file:
```yml
services:
  db:
    image: mariadb
    environment:
      MYSQL_ROOT_PASSWORD: root_password
      MYSQL_DATABASE: book_db
      MYSQL_USER: user
      MYSQL_PASSWORD: password
    ports:
      - "3306:3306"
  web:
    build: .
    ports:
      - "8080:8080"
    depends_on:
      - db
    environment:
      FLASK_ENV: development
      SQLALCHEMY_DATABASE_URI: mysql+pymysql://user:password@db/book_db
```


## Postman Collection
```json
{
    "info": {
        "name": "Book API",
        "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
    },
    "item": [
        {
            "name": "Get API Name",
            "request": {
                "method": "GET",
                "url": "http://localhost:8080/api/name"
            }
        },
        {
            "name": "Get All Books",
            "request": {
                "method": "GET",
                "url": "http://localhost:8080/books"
            }
        },
        {
            "name": "Create Book",
            "request": {
                "method": "POST",
                "url": "http://localhost:8080/books",
                "body": {
                    "mode": "raw",
                    "raw": "{ \"title\": \"Sample Book\", \"author\": \"Sample Author\" }"
                }
            }
        },
        {
            "name": "Get Book by ID",
            "request": {
                "method": "GET",
                "url": "http://localhost:8080/books/1"
            }
        },
        {
            "name": "Update Book by ID",
            "request": {
                "method": "PUT",
                "url": "http://localhost:8080/books/1",
                "body": {
                    "mode": "raw",
                    "raw": "{ \"title\": \"Updated Book Title\", \"author\": \"Updated Author\" }"
                }
            }
        },
        {
            "name": "Delete Book by ID",
            "request": {
                "method": "DELETE",
                "url": "http://localhost:8080/books/1"
            }
        },
        {
            "name": "Check Duplicate Book",
            "request": {
                "method": "POST",
                "url": "http://localhost:8080/api/check-duplicate",
                "body": {
                    "mode": "raw",
                    "raw": "{ \"title\": \"Sample Book\", \"author\": \"Sample Author\" }"
                }
            }
        }
    ]
}
```
