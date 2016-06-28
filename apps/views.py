from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from .models import Article
from django.contrib.auth.models import User
# Create your views here.


def home_page(request):
    article_list = Article.objects.all()
    return render(request, 'home.html', {'article_list': article_list})


def article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    user = get_object_or_404(User, pk=article.user.id)
    return render(
        request, 'view_article.html',
        {'article': article, 'user': user})


def about(request):
    return render(request, 'about.html',)
