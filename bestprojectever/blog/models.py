from django.db import models

# Create your models here.

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
    # author = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    author = models.CharField(max_length=255)
    # dla DateTimeField auto_now_add=True, aby automatycznie była uzupełniania data 
    # przy tworzeniu wpisu
    date = models.DateTimeField(auto_now_add=True)
