#!/bin/sh

echo "Waiting for database to be ready..."
while ! pg_isready -h db -p 5432 -q -U admin; do
  echo "Waiting for database..."
  sleep 2
done

echo "Starting the application..."
exec python start.py