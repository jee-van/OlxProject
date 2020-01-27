from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializers
from .models import Post
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class PostView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
