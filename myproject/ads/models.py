from django.db import models

import os
import time

priority_choices = ((x + 1, str(x + 1)) for x in xrange(5))

def generate_filename(instance, old_filename):
    extension = os.path.splitext(old_filename)[1]
    filename = str(time.time()) + extension
    return 'ads/' + filename

class Ad(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=generate_filename)
    link = models.URLField()
    priority = models.PositiveSmallIntegerField(choices=priority_choices,
                                                default=1)
    is_active = models.BooleanField(default=True)
    
    def __unicode__(self):
        return "Ad (%s)" % self.link
    
