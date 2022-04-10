from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class CustomUser(AbstractUser):
    username = models.CharField(blank=True, null=True, max_length=50)
    # Overwrtiting to available having a blank username, because the email field will be the main field 
    # used for authentication, for easier maintenanace
    email = models.EmailField('email address', unique=True)  
    # We have to overwrite this field from an AbstractUser model, 
    # to make the 'unique' constraint - so it will be available for using for the authentication
    USERNAME_FIELD = 'email'
    # That means that this field will be used for authentication
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    # Fields required by 'createsuperuser' command, username has to be there, otherwise Django will complain

    def __str__(self):
        return "{}".format(self.email)

class CustomUserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    date_of_birth = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    photo = models.ImageField(upload_to='uploads', blank=True)

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
    author = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name='articles')
    # author = models.CharField(max_length=255)
    # dla DateTimeField auto_now_add=True, aby automatycznie była uzupełniania data 
    # przy tworzeniu wpisu
    date = models.DateTimeField(auto_now_add=True)
