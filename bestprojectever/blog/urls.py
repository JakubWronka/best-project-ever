from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, ArticleViewSet

# każda aplikacja ma swoją konfigurację url
# oprócz dodania tutaj urlpatterns, 
# trzeba to zaimportować do głównego url configuration (urls.py w głównym folderze)

router = DefaultRouter()

router.register(r'users', CustomUserViewSet)
router.register(r'articles', ArticleViewSet)

urlpatterns = [
    path('', include(router.urls))
]
