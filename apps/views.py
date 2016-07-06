from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponseForbidden
from .models import Article
from django.contrib.auth.models import User
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def home_page(request):
    article_list = Article.objects.all()[0:10]
    return render(request, 'home.html', {'article_list': article_list})


def article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    user = get_object_or_404(User, pk=article.user.id)
    content = article.content

    edit_url = "/edit/" + str(article.id)

    return render(
        request, 'view_article.html',
        {
            'article': article, 'user': user,
            'content': content, 'edit_url': edit_url
        })


def about(request):
    return render(request, 'about.html',)


@login_required
def write(request, article_id=None):
    if article_id:
        article = get_object_or_404(Article, pk=article_id)
        if article.user != request.user:
            return HttpResponseForbidden()

    else:
        article = Article(user=request.user)

    form = ArticleForm(request.POST or None, instance=article)

    if request.method == 'POST':

        if form.is_valid():
            new_article = form.save(commit=False)
            new_article.save()
            article_id = new_article.id
            return redirect('/article/' + str(article_id))

    else:
        form = ArticleForm()
    return render(request, 'write_article.html', {'form': form})
