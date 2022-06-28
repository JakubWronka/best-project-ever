from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, ArticleViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# każda aplikacja ma swoją konfigurację url
# oprócz dodania tutaj urlpatterns, 
# trzeba to zaimportować do głównego url configuration (urls.py w głównym folderze)

router = DefaultRouter()

router.register(r'users', CustomUserViewSet)
router.register(r'articles', ArticleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('accounts/', include('allauth.urls')),
]
