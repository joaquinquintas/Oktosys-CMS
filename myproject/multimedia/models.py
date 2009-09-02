from django.db import models
from django import forms

import os
import time

def generate_filename(instance, old_filename):
    extension = os.path.splitext(old_filename)[1]
    filename = str(time.time()) + extension
    return 'multimedia/' + filename

class Photo(models.Model):
    title = models.CharField(max_length=255)
    added_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=generate_filename)
    
    def __unicode__(self):
        return self.title
    
