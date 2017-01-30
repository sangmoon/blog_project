from django.db import models
from django.contrib.auth.models import User
# Create your models here.

CATEGORY_CHOICES = (('python', 'python'), ('notice', 'notice'), ('etc', 'etc'))


class Image(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="image")


class Article(models.Model):

    user = models.ForeignKey(User, default=1)
    title = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length=2048)
    category = models.CharField(
        choices=CATEGORY_CHOICES,
        default='etc', max_length=10)
    # image = models.ManyToManyField(Image, blank=True)

    class Meta:
        ordering = ['-created_at']



