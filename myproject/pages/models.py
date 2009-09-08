from django.db import models
from tinymce import models as tinymce_models
import mptt

class Page(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    html = tinymce_models.HTMLField()
    parent = models.ForeignKey('self', blank=True, null=True,
                                       related_name='children')
    sort = models.CharField(max_length=255)
    show_fb_stream = models.BooleanField(default=False)
    
    def breadcrumbs(self):
        if self.parent:
            return self.parent.breadcrumbs() + [(self.slug, self.title)]
        return [(self.slug, self.title)]
    
    def __unicode__(self):
        if self.parent:
            return '%s/%s' % (self.parent.__unicode__(), self.title)
        return self.title
    
    def save(self):
        self.sort = self.__unicode__()
        super(Page, self).save()
    
    def get_absolute_url(self):
        """Return the absolute page url."""
        url = reverse('page', self.slug)
        return url
    
# Don't register the Page model twice.
try:
    mptt.register(Page)
except mptt.AlreadyRegistered:
    pass
