from django.db import models

class Entry(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)
    headline = models.CharField(max_length=255)
    slug = models.SlugField()
    excerpt = models.CharField(max_length=255)
    article = models.TextField()
    is_published = models.BooleanField()
