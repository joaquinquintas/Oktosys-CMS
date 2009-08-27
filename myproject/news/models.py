from django.db import models
from tinymce import models as tinymce_models

class Entry(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)
    headline = models.CharField(max_length=255)
    slug = models.SlugField()
    excerpt = models.TextField()
    article = tinymce_models.HTMLField()
    is_published = models.BooleanField()
    
    def __unicode__(self):
        return self.headline
    
