from django.shortcuts import render
from django.utils import timezone
from .models import Post

def header(request):
    return render(request, 'blog/header.html')

def posts(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/posts.html', {'posts': posts})

def charts(request):
    return render(request, 'blog/charts.html')

def home(request):
    return render(request, 'blog/home.html')
