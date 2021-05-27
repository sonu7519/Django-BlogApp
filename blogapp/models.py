from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField()
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    summary = models.TextField()