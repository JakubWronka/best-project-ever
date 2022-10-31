from __future__ import absolute_import, unicode_literals

from datetime import timedelta

from celery import shared_task
from celery.task import periodic_task
from celery.utils.log import get_task_logger

from .email import send_email_2

logger = get_task_logger(__name__)


@shared_task
def add(x, y):
    return x + y


@periodic_task(run_every=(timedelta(seconds=300)), name="send_email_task")
def send_email_task():
    logger.info("Sent review email")
    return send_email_2()
