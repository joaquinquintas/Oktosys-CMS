from django.db import models
from oembed.models import ProviderRule
# Create your models here.
class Link(models.Model):
    href = models.URLField()
    provider_rule = models.ForeignKey(ProviderRule)
    published = models.DateTimeField(null=True, blank=True)
    author = models.CharField(max_length=100, null=True, blank=True)
    
    @property
    def provider(self):
        return self.provider_rule.name