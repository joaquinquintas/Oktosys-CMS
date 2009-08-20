from django.db import models

class Highlight(models.Model):
    highlights = models.BooleanField()
    headline = models.CharField(max_length=255)
    description = models.TextField()
    icon_text = models.CharField(max_length=255)