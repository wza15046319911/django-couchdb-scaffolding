FROM python:3.11.3-alpine3.16
WORKDIR /app
#COPY requirements.txt /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]