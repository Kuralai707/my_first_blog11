from django.shortcuts import render
from django.shortcuts import render
from django.utils import timezone
from .models import Post
# Create your views here.
def main(request):
     return render(request, 'blog/boostrap.html', {})
def gallery(request):
     return render(request, 'blog/галерея.html', {})
def regis(request):
     return render(request, 'blog/регистрация.html', {})

def news(request):
     posts =	Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
     return render(request, 'blog/news.html', {'posts': posts})
