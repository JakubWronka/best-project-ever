from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_account_creation = models.DateField(auto_now_add=True)  # to discuss, might not be needed
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    # photo - field that stores files = to discuss
    # how should we handle Friends field/list
