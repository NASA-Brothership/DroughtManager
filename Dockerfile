FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip cache purge

# Install all dependencies from requirements.txt and show installed packages for debugging
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE ${BACKEND_PUBLISHED_PORT}

CMD ["python", "main.py"]
