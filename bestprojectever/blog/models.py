from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_account_creation = models.DateField(auto_now_add=True)  # to discuss, might not be needed
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    # photo - field that stores files = to discuss
    # how should we handle Friends field/list

# Utworzenie modelu Article dla posta/wpisu na blogu
class Article(models.Model):
    # typ pól wg dostępnych na stronie
    # https://docs.djangoproject.com/en/4.0/ref/models/fields/
    # dla CharField argument max_length jests mandatory wg info na stronie 
    # https://docs.djangoproject.com/en/4.0/ref/models/fields/#charfield
    title = models.CharField(max_length=255)
    content = models.TextField()
    # Używam ForeignKey z uwagi na potrzebę stworzenia relacji One To Many 
    # (jeden autor może mieć wiele artykułów), do tego służy ForeignKey
    # opcja on_delete jako DO_NOTHING, żeby przy usunięciu konta Clienta (użytkownika), 
    # jego wpisy wraz z informacją, że był autorem pozostały nieusunięte
    # docelowo pole author powinno być zastąpione linijką poniżej, podstawiając nazwę modelu
    # w miejsce "Client"
    # zapoznać się z related_name
    # author = models.ForeignKey(Client, on_delete=models.DO_NOTHING, related_name='articles')
    author = models.CharField(max_length=255)
    # dla DateTimeField auto_now_add=True, aby automatycznie była uzupełniania data 
    # przy tworzeniu wpisu
    date = models.DateTimeField(auto_now_add=True)
