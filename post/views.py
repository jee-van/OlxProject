from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializers
from .models import Post
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.views.generic import TemplateView

class PostView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class index(TemplateView):
    template_name = 'index.html'