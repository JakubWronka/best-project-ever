from django.template import Context
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings

from .models import Article, CustomUser

def send_email_2():
    for user in CustomUser.objects.all():
        send_send(user)


def send_send(user):
    context = {
        'name': user.username,
        'last_article_1_title': Article.objects.order_by('-pk')[0].title,
        'last_article_1_content': Article.objects.order_by('-pk')[0].content,
        'last_article_2_title': Article.objects.order_by('-pk')[1].title,
        'last_article_2_content': Article.objects.order_by('-pk')[1].content,
        'last_article_3_title': Article.objects.order_by('-pk')[2].title,
        'last_article_3_content': Article.objects.order_by('-pk')[2].content,
    }

    email_subject = 'Your best project ever newsletter'
    email_body = render_to_string('email_message.txt', context)

    email = EmailMessage(
        email_subject, email_body,
        settings.DEFAULT_FROM_EMAIL, [user.email,],
    )
    return email.send(fail_silently=False)

