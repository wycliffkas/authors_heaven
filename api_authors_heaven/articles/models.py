from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=200)
