from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Article(models.Model):

    user = models.ForeignKey(User, default=None)
    title = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length=2048)

    class Meta:
        ordering = ['-created_at']
