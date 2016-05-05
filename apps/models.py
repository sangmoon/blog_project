from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.


class Article(models.Model):

    user = models.ForeignKey(User, default=None)
    title = models.CharField(max_length=200)
    created_time = models.DateTimeField(default=datetime.now)
    content = models.TextField()

    class Meta:
        ordering = ['-created_time']
