from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bestprojectever.settings')

app = Celery('bestprojectever')

app.config_from_object('django.conf:settings', namespace='CELERY')

# tu testuje beat:
# app.conf.beat_schedule = {
#     'add-every-30-seconds': {
#         'task': 'blog.tasks.send_email_task',
#         'schedule': 30.0,
#         'args': ("asd")
#     },
# }

app.autodiscover_tasks()
