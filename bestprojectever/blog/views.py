from django.views.generic import ListView, DetailView
from .models import CustomUser

class CustomUserListView(ListView):
    model = CustomUser

class CustomUserDetailView(DetailView):
    model = CustomUser