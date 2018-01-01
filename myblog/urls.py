"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from apps import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    path('test', views.test, name="test"),
    path('admin', admin.site.urls),
    path('article/<int:article_id>', views.article, name='article'),
    path('about', views.about, name='about'),
    path('write', views.write, name='write'),
    path('edit/<int:article_id>', views.write, name='edit'),
    path('login', login, name='login',
         kwargs={
            'template_name': 'login.html'
         }),
    path('logout', logout, name='logout',
         kwargs={
            'template_name': 'logout.html',
         }),
    path('markdown', views.view_markdown, name='md'),
    path('', views.home_page, name='home_page'),
]
