import os
import environ
from celery import Celery




BASE_DIR = os.path.dirname(os.path.abspath(__file__))
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, 'easytasks/settings/.env.'+env('RAILWAY_ENVIRONMENT')))

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'easytasks.settings.'+env('RAILWAY_ENVIRONMENT'))

app = Celery('easytasks')

app.config_from_object('easytasks.settings.'+env('RAILWAY_ENVIRONMENT'), namespace='CELERY')

app.autodiscover_tasks()


