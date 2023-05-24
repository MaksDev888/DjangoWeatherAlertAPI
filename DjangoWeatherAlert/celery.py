import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoWeatherAlert.settings")

app = Celery("DjangoWeatherAlert")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


app.conf.beat_schedule = {
    "update_weather_every_one_hour": {"task": "Constant updates", "schedule": crontab(minute=0, hour="*/1")},
    "send_email_every_one_hour": {
        "task": "Preparing to send e-mail every one hour",
        "schedule": crontab(minute=0, hour="*/1"),
    },
    "send_email_every_three_hours": {
        "task": "Preparing to send e-mail every three hours",
        "schedule": crontab(minute="*/3"),
    },
    "send_email_every_six_hours": {
        "task": "Preparing to send e-mail every six hours",
        "schedule": crontab(minute=0, hour="*/6"),
    },
}
