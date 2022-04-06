from dataclasses import field
from operator import mod
from rest_framework import serializers
from .models import CustomUser, Article

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined', 'date_of_birth', 'bio', 'location']
        # I got the field names from AbstractBaseUser (password), AbstractUser () and our CustomUser (the rest of the fields) classes
        # id is a primary key from the database

class ArticleSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer(read_only=True)
    # By default, only primary key of an author will be displayed - by that we display all the fields that are included in CustomUserSerializer
    class Meta:
        model = Article
        fields = '__all__'
        # When all fields from the model are meant to be used, we don't need to specify them one by one, but instead just use '__all__' to get all fields
