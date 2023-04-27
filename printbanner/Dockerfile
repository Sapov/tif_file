FROM python:3.10-alpine
WORKDIR /django
COPY .. /django
RUN apk update && pip install -r /django/requirements_prod.txt --no-cache-dir
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]