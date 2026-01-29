FROM python:3.8-slim-bullseye

RUN apt-get update -y && apt-get install -y gcc g++

WORKDIR /app

# 1. Copy everything first so setup.py and src/ are available
COPY . /app

# 2. Now install requirements (including the -e . local package)
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port ${PORT:-8080}"]