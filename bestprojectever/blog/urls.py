from django.urls import path
from .views import CustomUserListView, CustomUserDetailView

urlpatterns = [
    path('users/', CustomUserListView.as_view()),
    path('users/<int:pk>/', CustomUserDetailView.as_view()),
]