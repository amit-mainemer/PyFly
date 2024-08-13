#!/bin/sh
# entry.sh

while ! pg_isready -h db -p 5432 -q -U admin; do
  echo "Waiting for database to be ready..."
  sleep 2
done


exec set PYTHONPATH=./

flask db upgrade

flask seed run


exec flask run --host=0.0.0.0