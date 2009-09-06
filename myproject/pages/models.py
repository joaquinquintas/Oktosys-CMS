from django.db import models
from tinymce import models as tinymce_models

class Page(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    html = tinymce_models.HTMLField()
    parent = models.ForeignKey('self', blank=True, null=True,
                                       related_name='children')
    sort = models.CharField(max_length=255)
    
    def breadcrumbs(self):
        if self.parent:
            return self.parent.breadcrumbs() + [self.title]
        return [self.title]
    
    def __unicode__(self):
        if self.parent:
            return '%s/%s' % (self.parent.__unicode__(), self.title)
        return self.title
    
    def save(self):
        self.sort = self.__unicode__()
        super(Page, self).save()
    
