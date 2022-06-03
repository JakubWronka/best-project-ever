from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Article, CustomUser, CustomUserProfile

@receiver(post_save, sender=CustomUser)
def create_article_for_new_user(sender, **kwargs):
    if kwargs['created']:
        user_number = kwargs['instance'].first_name
        Article.objects.create(author=kwargs['instance'], title='New user added!', 
        content='Next user {user} is added'.format(user=user_number))
