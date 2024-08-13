FROM python:3.9-slim

WORKDIR /server

ENV PYTHONPATH=/server

# Install necessary packages
RUN apt-get update && \
    apt-get install -y \
    gcc \
    libpq-dev \
    postgresql-client

# Copy application files
COPY . .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install pytest


RUN ls -l /server

# Ensure entry.sh is executable
RUN chmod +x /server/entry.sh

# Expose the application port
EXPOSE 5000

# Set the default command
CMD ["/server/entry.sh"]
