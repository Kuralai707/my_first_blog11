from django.shortcuts import render

# Create your views here.
def main(request):
     return render(request, 'blog/boostrap.html', {})
def gallery(request):
     return render(request, 'blog/галерея.html', {})
def regis(request):
     return render(request, 'blog/регистрация.html', {})
