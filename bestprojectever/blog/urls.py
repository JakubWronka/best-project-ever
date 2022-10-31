from django.urls import include, path
from graphene_django.views import GraphQLView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from blog.schema import schema

from .views import ArticleViewSet, CustomUserViewSet

router = DefaultRouter()

router.register(r"users", CustomUserViewSet)
router.register(r"articles", ArticleViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("graphql/", GraphQLView.as_view(graphiql=True, schema=schema)),
]
