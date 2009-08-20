from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    html = models.TextField()
    parent = models.ForeignKey('self', blank=True, null=True,
                                       related_name='children')
    
    def __unicode__(self):
        return self.title
    
