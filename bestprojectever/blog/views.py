from django.views.generic import ListView, DetailView
from .models import CustomUser, Article

class CustomUserListView(ListView):
    # class-based view, inheriting from a ListView class, with model variable set to a CustomUser model
    # needed to display all CustomUser class objects
    model = CustomUser

class CustomUserDetailView(DetailView):
    # class-based view, inheriting from a DetailView class, with model variable set to a CustomUser model
    # needed to display a specific CustomUser class object
    model = CustomUser

class ArticleListView(ListView):
    model = Article

class ArticleDetailView(DetailView):
    model = Article
