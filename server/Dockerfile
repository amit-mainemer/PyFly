FROM python:3.9-slim

WORKDIR /server

ENV PYTHONPATH=/server

RUN apt-get update && \
    apt-get install -y \
    gcc \
    libpq-dev \
    postgresql-client

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN pip install pytest

RUN chmod +x /server/entry.sh

EXPOSE 5000

CMD ["./entry.sh"]
