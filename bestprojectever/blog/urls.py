from django.urls import path
from .views import CustomUserListView, CustomUserDetailView

urlpatterns = [
    path('users/', CustomUserListView.as_view()),
    # link to users endpoint, with a class-based view passed as a parameter, showing all users in a list
    path('users/<int:pk>/', CustomUserDetailView.as_view()),
    # link to user/user_id endpoint, with a class-based view passed as a parameter, showing a user with a user_id specified in the link
]
