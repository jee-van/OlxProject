from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class PostSerializers(serializers.ModelSerializer):
    author = UserSerializers(many=False, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'discription', 'author']