from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('post', views.PostView)

urlpatterns = [
    path('', include(router.urls))
]