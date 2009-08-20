from django.db import models

import os
from django.template.defaultfilters import slugify

def generate_icon_filename(instance, old_filename):
    extension = os.path.splitext(old_filename)[1]
    filename = slugify(instance.headline) + '.' + extension
    return 'icons/' + filename

class Highlight(models.Model):
    headline = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.ImageField(upload_to=generate_icon_filename)
    icon_text = models.CharField(max_length=255)
