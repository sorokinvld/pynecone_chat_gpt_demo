FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    curl \
    && curl -fsSL https://deb.nodesource.com/setup_19.x | bash - \
    && apt-get update && apt-get install -y \
    nodejs \
    unzip \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN pip install wheel && pip install -r requirements.txt
RUN pc init

CMD ["pc","run"]

EXPOSE 3000
EXPOSE 8000
