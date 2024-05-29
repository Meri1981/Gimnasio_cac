# Gimnasio_cac

Desarrollo de un proyecto de gestión con Django

1. para crear archivo .env:
   pip install python-decouple
   crear archivo .env con el siguiente contenido, reemplazando #:
   DB_ENGINE=django.db.backends.postgresql
   DB_NAME=gimnasio_cac
   DB_USER=postgres
   DB_PASSWORD=#
   DB_HOST=127.0.0.1
   DB_PORT=5432

en settings.py reemplazar lo siguiente:
from decouple import config

DATABASES = {
"default": {
"ENGINE": config('DB_ENGINE'),
"NAME": config('DB_NAME'),
"USER": config('DB_USER'),
"PASSWORD": config('DB_PASSWORD'),
"HOST": config('DB_HOST'),
"PORT": config('DB_PORT'),
}
}

2. pip install psycopg2
   crear en postgres una base de datos nombre gimnasio_cac
   python manage.py migrate
