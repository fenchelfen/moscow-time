FROM python:3.7

ENV PYTHONUNBUFFERED 1
ENV SECRET_KEY "50w&tg&)2=%ia6pbl9)4@*7p4l()jb2q$5h" # dummy secret key

WORKDIR /app

COPY requirements.txt .
RUN pip install --cache-dir=/cache -r requirements.txt

COPY . .

CMD python3 manage.py migrate && daphne -b 0.0.0.0 -p 8000 moscow.asgi:application
