from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponseForbidden, HttpResponse, JsonResponse
from .models import Article
from django.contrib.auth.models import User
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
from .templatetags.markdownify import markdown
from .models import CATEGORY_CHOICES

# Create your views here.


def test(request):
    return render(request, 'test.html')


def home_page(request):
    article_list = Article.objects.all()
    return render(
        request, 'home.html',
        {'article_list': article_list, 'choices': CATEGORY_CHOICES},
    )


def article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    user = get_object_or_404(User, pk=article.user.id)

    edit_url = "/edit/" + str(article.id)

    return render(
        request, 'view_article.html',
        {
            'article': article, 'user': user,
            'content': markdown(article.content), 'edit_url': edit_url
        })


def about(request):
    return render(request, 'about.html',)


@login_required
def write(request, article_id=None):

    # edit form
    # get && id
    if article_id and request.method == "GET":
        article = get_object_or_404(Article, pk=article_id)
        if article.user != request.user:
            return HttpResponseForbidden()
        else:
            form = ArticleForm(request.POST or None, instance=article)
            return render(request, 'write_article.html', {'form': form})

    # get && not id
    elif article_id:
        article = get_object_or_404(Article, pk=article_id)

    else:
        article = Article(user=request.user)

    form = ArticleForm(request.POST or None, instance=article)
# 글 제출
# POST click
    if request.method == 'POST':
        if form.is_valid():
            new_article = form.save(commit=False)
            new_article.save()
            article_id = new_article.id
            return redirect('/article/' + str(article_id))
# 글 새로 만들기
    else:
        form = ArticleForm()
    return render(request, 'write_article.html', {'form': form})


def view_markdown(request):
    data = {
        'md_js': markdown(request.GET.get('content'))
    }
    return JsonResponse(data)
