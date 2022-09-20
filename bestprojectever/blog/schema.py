from concurrent.futures.process import BrokenProcessPool
import graphene
from graphene_django import DjangoObjectType, DjangoListField
from .models import Article, CustomUserProfile, CustomUser

class ArticlesType(DjangoObjectType):
    class Meta:
        model = Article
        fields = ('title', 'author', 'date')

class CustomUsersType(DjangoObjectType):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'first_name')



class Query(graphene.ObjectType):
    all_articles = graphene.List(ArticlesType)

    def resolve_all_articles(root, info):
        return Article.objects.all()

schema = graphene.Schema(query=Query)
