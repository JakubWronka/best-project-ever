from concurrent.futures.process import BrokenProcessPool
import graphene
from graphene_django import DjangoObjectType
from .models import Article, CustomUserProfile

class ArticlesType(DjangoObjectType):
    class Meta:
        model = Article
        fields = ('title', 'content')


class Query(graphene.ObjectType):
    all_articles = graphene.List(ArticlesType)

    def resolve_all_articles(root, info):
        return Article.objects.all()

schema = graphene.Schema(query=Query)
