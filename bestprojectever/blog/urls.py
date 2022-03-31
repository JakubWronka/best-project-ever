from django.urls import path

from .views import ArticleDetailView, ArticleListView

# każda aplikacja ma swoją konfigurację url
# oprócz dodania tutaj urlpatterns, 
# trzeba to zaimportować do głównego url configuration (urls.py w głównym folderze)
urlpatterns = [
    # poniżej dodaję co ma wywoływać django jeżeli do adresu na końcu dodam "articles/"
    path('articles/', ArticleListView.as_view()),
    path('articles/<int:pk>', ArticleDetailView.as_view()),
]