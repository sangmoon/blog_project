from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Article
from django.contrib.auth.models import User
from .forms import ArticleForm
# Create your views here.


def home_page(request):
    article_list = Article.objects.all()[0:10]
    return render(request, 'home.html', {'article_list': article_list})


def article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    user = get_object_or_404(User, pk=article.user.id)
    content = article.content

    return render(
        request, 'view_article.html',
        {'article': article, 'user': user, 'content': content, })


def about(request):
    return render(request, 'about.html',)


def write(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article_title = request.POST['title']
            article_content = request.POST['content']
            new_article = Article.objects.create(
                title=article_title,
                content=article_content,
            )
            pk = new_article.id
            return redirect('/article/' + str(pk))
    else:
        form = ArticleForm()
    return render(request, 'write_article.html', {'form': form})
