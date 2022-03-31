from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from blog.models import Article

# Create your views here.
# tutaj definiuję funkcję, która korzysta z django ORM i przetwarza request
# def articles_view(request):
    # poniżej przypisuję do "query_set" zapytanie do bazy danych (ono nie jest wywoływane
    # tutaj, tylko jest "przygotowywane na później")
    # query_set = Article.objects.all()

    # poniżej definuję co ma być zwrócone (metoda render bierze request oraz template html'owy,
    # oraz jako trzeci argument słownik, do którego później będę się mógł odwołać w templatce articles.html)
    # return render(request, 'articles.html', { 
    #     'name': 'Mosh',
    #     'articles': list(query_set)
    #     })

class ArticleListView(ListView):
    model = Article

class ArticleDetailView(DetailView):
    model = Article
