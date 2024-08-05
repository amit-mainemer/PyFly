Here's the complete `README.md` content for your project:

# Project Name

## Description

This project is a web application with a React frontend, a Flask backend, and a PostgreSQL database. It uses Docker for containerization.

## Prerequisites

- Docker
- Docker Compose

## Setup

### Environment Variables

Create a `.env` file in the root directory of the project with the following environment variables:

```bash
POSTGRES_USER=your_postgres_user
POSTGRES_PASSWORD=your_postgres_password
POSTGRES_DB=your_postgres_db
JWT_TOKEN=your_jwt_token
REACT_APP_API_URL=http://localhost:5000
```

### Docker Compose

To build and start the application, run:

```bash
docker-compose up --build
```

This command will build the Docker images and start the containers for the database, backend server, and frontend client.

## Run

To start the application in detached mode, run:

```bash
docker-compose up -d
```

This will start all the services defined in the `docker-compose.yml` file in the background.

### Initial Setup

If this is the first time setting up the project, you need to manually create the tables in the database. Follow these steps:

1. **Start the containers** using Docker Compose:

    ```bash
    docker-compose up -d
    ```

2. **Access the server container**:

    ```bash
    docker exec -it flask_server_container_name /bin/sh
    ```

3. **Run the database migrations** to create the tables:

    ```bash
    flask db migrate -m "init"
    ```

4. **Run the database migrations** to create the tables:

    ```bash
    flask db upgrade
    ```

5. **Seed the database** if needed:

    ```bash
    flask seed run
    ```

Replace `flask_server_container_name` with the actual name or ID of your Flask server container.

### Notes

- **Automatic Migrations:** The third step is necessary only if its the first time running the project

- **Debugging:** If you encounter issues with the database or migrations, ensure that the database container is up and running and that the connection details in the `.env` file are correct.

## Testing

To run tests, use the following command:

```bash
docker-compose exec server pytest
```

## Cleanup

To stop and remove all containers, networks, and volumes created by Docker Compose, use:

```bash
docker-compose down -v
```

## Contributing

Please follow the guidelines for contributing to this project outlined in the `CONTRIBUTING.md` file.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
```

You can save this content into a `README.md` file for your project.