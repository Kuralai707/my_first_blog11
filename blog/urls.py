from django.urls import path
from . import views
urlpatterns = [
    path('', views.main, name='main'),
path ('gallery', views.gallery, name='gallery'),
    path ('regis', views.regis, name='regis'),
    ]
