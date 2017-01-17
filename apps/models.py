from django.db import models
from django.contrib.auth.models import User
# Create your models here.

CATEGORY_CHOICES = ((1, ('python')), (2, ('notice')), (3, ('etc')))


class Article(models.Model):

    user = models.ForeignKey(User, default=1)
    title = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length=2048)
    category = models.IntegerField(choices=CATEGORY_CHOICES, default=3)

    class Meta:
        ordering = ['-created_at']
