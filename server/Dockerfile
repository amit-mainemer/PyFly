FROM python:3.9-slim

WORKDIR /server

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    postgresql-client

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN pip install pytest

EXPOSE 5000

CMD ["./entrypoint.sh"]
