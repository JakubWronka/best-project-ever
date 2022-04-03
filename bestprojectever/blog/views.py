from rest_framework import viewsets
from .models import CustomUser, Article
from .serializers import CustomUserSerializer, ArticleSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()

class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
