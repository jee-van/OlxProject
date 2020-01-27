from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=100)
    discription = models.TextField()
    author = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    post_created_on = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return self.title