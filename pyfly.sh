

function pyfly() {
    case "$1" in
        "init")
            docker compose up -d --build && docker-compose exec server bash flask db init && docker-compose exec server bash flask db migrate -m "init" && docker-compose restart server
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
        *)
            echo "please enter the following options [init, local_db, tests, server_rebuild]"
        ;;
    esac
}