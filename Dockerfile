FROM python:3.8-slim

WORKDIR /app

RUN apt-get update -y
RUN apt-get install 'ffmpeg'\
    'libsm6'\
    'libgl1'\
    'libxext6'  -y

COPY requirements.txt .
RUN pip install --no-deps -r requirements.txt

COPY . .

EXPOSE 80

CMD ["gunicorn" "--bind=0.0.0.0" "--timeout 600" "--workers 3" "--worker-class" "uvicorn.workers.UvicornWorker" "app:app" ]
