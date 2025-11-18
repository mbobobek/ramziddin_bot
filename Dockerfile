FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV TOKEN=8543015458:AAEYmTX6zthB35WqM7MjWFQ5FyfH2Q3XnKU

CMD ["python", "bot.py"]
