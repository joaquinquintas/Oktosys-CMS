from django.db import models
# Create your models here.
class Link(models.Model):
    href = models.URLField()
    date = models.DateTimeField(null=True, blank=True)
