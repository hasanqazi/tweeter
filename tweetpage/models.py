from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tweet(models.Model):
  body = models.TextField()
  slug = models.SlugField()
  date = models.DateTimeField(auto_now_add=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
