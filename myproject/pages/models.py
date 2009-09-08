from django.db import models
from tinymce import models as tinymce_models
import mptt
from django.utils.safestring import mark_safe 
from django.core.urlresolvers import reverse

def get_slug_and_relative_path(path):
    """Return the page's slug and relative path."""
    root = reverse('pages-root')
    if path.startswith(root):
        path = path[len(root):]
    if len(path) and path[-1] == '/':
        path = path[:-1]
    slug = path.split("/")[-1]
    lang = None
    return slug, path

class PageManager(models.Manager):
    """
    Page manager provide several filters to obtain pages :class:`QuerySet`
    that respect the page settings.
    """
    
    def on_site(self, site_id=None):
        return self

    def root(self):
        """Return a :class:`QuerySet` of pages without parent."""
        return self.filter(parent__isnull=True)

    def navigation(self):
        """Creates a :class:`QuerySet` of the published root pages."""
        return self.root()

    def hidden(self):
        """Creates a :class:`QuerySet` of the hidden pages."""
        return None

    def filter_published(self, queryset):
        return queryset

    def published(self):
        """Creates a :class:`QuerySet` of published filter."""
        return self.filter_published(self)

    def drafts(self):
        return None

    def expired(self):
        return None

    def from_path(self, complete_path, exclude_drafts=True):
        """Get a page according to the page's path."""
        slug, path  = get_slug_and_relative_path(complete_path)
        pages_list = self.on_site().filter(slug=slug)
        current_page = None
        if len(pages_list) == 1:
            return pages_list[0]
        # more than one page matching the slug, let's use the full url
        if len(pages_list) > 1:
            for page in pages_list:
                if page.get_url(lang) == complete_path:
                    return page
        return None

class Page(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    html = tinymce_models.HTMLField()
    parent = models.ForeignKey('self', blank=True, null=True,
                                       related_name='children')
    sort = models.CharField(max_length=255)
    show_fb_stream = models.BooleanField(default=False)
    objects = PageManager()
    
    def breadcrumbs(self):
        if self.parent:
            return self.parent.breadcrumbs() + [(self.slug, self.title)]
        return [(self.slug, self.title)]
    
    def __unicode__(self):
        return "%s" % self.with_level().replace(" ", "|", 1).replace(" ", "-")
    
    def save(self):
        self.sort = self.__unicode__()
        super(Page, self).save()
    def valid_targets(self, perms="All"):
        """Return a :class:`QuerySet` of valid targets for moving a page into the
        tree.

        :param perms: the level of permission of the concerned user.
        """
        exclude_list = [self.id]
        for p in self.get_descendants():
            exclude_list.append(p.id)
            return Page.objects.exclude(id__in=exclude_list)

    def get_url(self, language=None):
        """Return url of this page, adding all parent's slug."""
#        url = cache.get('page_key_%s' % self.id)
#        if url:
#            return url
#        else:
#            url = u'%s' % self.slug
        url = u'%s' % self.slug # Remove this line when enabling cache
        for ancestor in self.get_ancestors(ascending=True):
            url = ancestor.slug + u'/' + url 

#        cache.set('page_key_%s' % self.id, url)

        return "/pages/%s" % url
    def with_level(self):
        """Display the slug of the page prepended with insecable
        spaces equal to the level of page in the hierarchy."""
        level = ''
        if self.level:
            for n in range(0, self.level):
                level += '   '
        return mark_safe(level + self.slug)

    def get_children_for_frontend(self):
        """Return a :class:`QuerySet` of published children page"""
        return self.get_children()

    def margin_level(self):
        return self.level * 2    
    def get_absolute_url(self):
        """Return the absolute page url."""
        url = reverse('page', self.slug)
        return url

    class Meta:
        """Make sure the ordering is correct."""
        ordering = ['tree_id', 'lft']
        verbose_name = 'page'
        verbose_name_plural = 'pages'   
        
# Don't register the Page model twice.
try:
    mptt.register(Page)
except mptt.AlreadyRegistered:
    pass
