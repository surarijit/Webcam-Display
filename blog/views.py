from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'blog/index.html', {})

def base(request):
    return render(request, 'blog/base.html', {})
