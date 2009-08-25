from django.db import models

import os

def generate_image_filename(instance, old_filename):
    extension = os.path.splitext(old_filename)[1]
    filename = instance.page.slug + extension
    return 'sponsor/' + filename

class Sponsor(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to=generate_image_filename)
