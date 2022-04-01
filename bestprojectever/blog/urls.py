from django.urls import path
from .views import CustomUserListView, CustomUserDetailView
from .views import ArticleDetailView, ArticleListView

# każda aplikacja ma swoją konfigurację url
# oprócz dodania tutaj urlpatterns, 
# trzeba to zaimportować do głównego url configuration (urls.py w głównym folderze)

urlpatterns = [
    path('users/', CustomUserListView.as_view()),
    # link to users endpoint, with a class-based view passed as a parameter, showing all users in a list
    path('users/<int:pk>/', CustomUserDetailView.as_view()),
    # link to user/user_id endpoint, with a class-based view passed as a parameter, showing a user with a user_id specified in the link
    # poniżej dodaję co ma wywoływać django jeżeli do adresu na końcu dodam "articles/"
    path('articles/', ArticleListView.as_view()),
    path('articles/<int:pk>', ArticleDetailView.as_view()),
]
