from django.contrib import admin
from apps.models import Article
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'content', 'created_at', 'updated_at')

admin.site.register(Article, ArticleAdmin)
# 2개를 같이 등록해야 함에 주의하자
