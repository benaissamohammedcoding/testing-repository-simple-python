FROM python:3.9-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

FROM python:3.9-slim

WORKDIR /app

COPY . .

COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages

ENV FLASK_APP=app.py
ENV FLASK_ENV=production
ENV PORT=8888  

EXPOSE $PORT

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8888", "app:application"]

