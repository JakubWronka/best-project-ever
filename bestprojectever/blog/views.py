from rest_framework import viewsets, renderers
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import CustomUser, Article
from .serializers import CustomUserSerializer, ArticleSerializer

from .permissions import IsLoggedInUserOrAdmin, IsAdminUser


class CustomUserViewSet(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    renderer_classes = (renderers.JSONRenderer, renderers.TemplateHTMLRenderer)
    
    def list(self, request, *args, **kwargs):
        response = super(ArticleViewSet, self).list(request, *args, **kwargs)
        #if request.accepted_renderer.format == 'html':
        return Response({'article_list': response.data}, template_name='blog/article_list.html')

    def retrieve(self, request, pk=None, *args, **kwargs):
        response = super(ArticleViewSet, self).retrieve(request, pk, *args, **kwargs)
        return Response({'article': response.data}, template_name='blog/article_detail.html')



