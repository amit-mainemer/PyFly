INFO_MESSAGE="\033[1;34mUsage: pyfly [option]\033[0m\n\033[1;32mOptions:\033[0m\n\033[1;33m  start\033[0m            Start and build the Docker containers in detached mode.\n\033[1;33m  db_setup\033[0m         Run database migrations using Flask.\n\033[1;33m  local_db\033[0m         Run a local PostgreSQL container on port 5433.\n\033[1;33m  tests\033[0m            Execute the test suite using pytest.\n\033[1;33m  lint\033[0m             Run pylint for code linting.\n\033[1;33m  server_rebuild\033[0m   Rebuild and restart the server container.\n\033[1;33m  client_rebuild\033[0m   Rebuild and restart the client container.\n\033[1;33m  open_postgres\033[0m    Open a bash shell in the PostgreSQL container.\n\033[1;33m  open_redis\033[0m       Open a bash shell in the Redis container."

function pyfly() {
    case "$1" in
        "start")
            docker compose up -d --build
        ;;
        "db_setup")
            docker-compose exec server bash flask db upgrade
        ;;
        "local_db")
            docker run  -d \
            -e POSTGRES_USER=admin \
            -e POSTGRES_PASSWORD=123 \
            -e POSTGRES_DB=pyfly \
            -p 5433:5432 \
            -v postgres_data:/var/lib/postgresql/data \
            postgres:13
        ;;
        "tests")
            docker-compose exec server bash -c "PYTHONPATH=. pytest -s"
        ;;
        "lint")
            docker-compose exec server bash -c "pylint ."
        ;;
        "server_rebuild")
            docker compose build server && docker compose up -d
        ;;
        "client_rebuild")
            docker compose build client && docker compose up -d
        ;;
        "open_postgres")
           docker exec -it flask_postgres /bin/bash
        ;;
        "open_redis")
            docker exec -it redis-1 /bin/bash
        ;;
        *)
            echo -e "$INFO_MESSAGE"
        ;;
    esac
}