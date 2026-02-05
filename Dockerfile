FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy API code from api/ to app/api 
COPY api/ api/

# Create logs directory inside container
RUN mkdir /logs

EXPOSE 8000

CMD ["sh", "-c", "uvicorn api.main:app --host 0.0.0.0 --port $PORT"]