# Dockerfile for MCP server (src layout)
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src /app/src

EXPOSE 7000

CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "7000"]
