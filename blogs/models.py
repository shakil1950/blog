from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    craeted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

