from django.db import models

import os
from django.template.defaultfilters import slugify

def generate_image_filename(instance, old_filename):
    extension = os.path.splitext(old_filename)[1]
    filename = slugify(instance.title) + extension
    return 'sponsor/' + filename

class Sponsor(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to=generate_image_filename)
    link = models.URLField()
    
    def __unicode__(self):
        return "Sponsor (%s, %s)" % (self.name, self.title)
    
