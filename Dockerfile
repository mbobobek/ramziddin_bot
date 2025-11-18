FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV TOKEN=8543015458:AAFeHaW1ixq_c7JP4F3ZDEzRqMOVt2PWZJI

CMD ["python", "bot.py"]
