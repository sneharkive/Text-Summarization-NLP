FROM python:3.8-slim-bullseye

RUN apt-get update -y && apt-get install -y gcc g++

WORKDIR /app

# Copy all files (including setup.py and src/) first
COPY . /app

# Install requirements (this will now find setup.py for the '-e .' line)
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port ${PORT:-8080}"]