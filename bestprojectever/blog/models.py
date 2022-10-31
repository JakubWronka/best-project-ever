from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = models.CharField(blank=True, null=True, max_length=50)
    # Overwrtiting to make it available to have a blank username, because the email field will be the main field
    # used for authentication, for easier maintenanace
    email = models.EmailField("email address", unique=True)
    # We have to overwrite this field from an AbstractUser model,
    # to make the 'unique' constraint - so it will be available for using for the authentication
    USERNAME_FIELD = "email"
    # That means that this field will be used for authentication
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]
    # Fields required by 'createsuperuser' command, username has to be there, otherwise Django will complain

    def __str__(self):
        return "{}".format(self.email)


class CustomUserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile"
    )
    date_of_birth = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    photo = models.ImageField(upload_to="uploads", blank=True)


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(
        CustomUser, on_delete=models.DO_NOTHING, related_name="articles"
    )
    created_at = models.DateTimeField(auto_now_add=True)
