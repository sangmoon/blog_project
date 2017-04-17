from django.db import models
from django.contrib.auth.models import User
# Create your models here.

CATEGORY_CHOICES = (
    ('python', 'python'), ('vue', 'vue'),
    ('notice', 'notice'), ('etc', 'etc'))


class Article(models.Model):

    user = models.ForeignKey(User, default=1)
    title = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length=9192)
    category = models.CharField(
        choices=CATEGORY_CHOICES,
        default='etc', max_length=10)

    class Meta:
        ordering = ['-created_at']



