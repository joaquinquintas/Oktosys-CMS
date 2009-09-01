from django.db import models
from tinymce import models as tinymce_models

class Page(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    html = tinymce_models.HTMLField()
    parent = models.ForeignKey('self', blank=True, null=True,
                                       related_name='children')
    
    def __unicode__(self):
        return self.title
    
