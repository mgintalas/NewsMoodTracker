from django.shortcuts import render
from .models import Article

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'sentiment_analysis/article_list.html', {'articles': articles})

def home(request):
    return render(request, 'sentiment_analysis/home.html')