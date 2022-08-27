import os

from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webscrap_dw.settings')

app = Celery('webscrap_dw',
                include=['webscrap_dw.tasks'])

# Timezone:
app.conf.timezone = 'Europe/London'

# Execute daily update at midnight.
app.conf.beat_schedule = {
    'daily-update': {
        'task': 'webscrap',  #name='webscrap'   tasks.add
        'schedule': crontab(minute=0, hour=0),
        'args': (16, 16),
    },
}

# configure the location of your Redis database:
app.conf.broker_url = 'redis://localhost:6379/0'
app.conf.result_backend = 'redis://localhost:6379/0'


# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')