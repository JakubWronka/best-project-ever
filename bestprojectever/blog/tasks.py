from __future__ import absolute_import, unicode_literals
from datetime import timedelta

# from celery import Celery
from celery.task import periodic_task
from celery.schedules import crontab
from celery import shared_task
from celery.decorators import task
from celery.utils.log import get_task_logger

from .email import send_email_2


logger = get_task_logger(__name__)

@shared_task
def add(x, y):
    return x + y


# @task(name="send_email_task")
# @shared_task
# @periodic_task(name='send_email_task', run_every=crontab())
@periodic_task(run_every=(timedelta(seconds=30)), name='send_email_task')
def send_email_task():
    logger.info("Sent review email")
    return send_email_2()
