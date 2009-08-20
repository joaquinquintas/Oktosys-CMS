from django.db import models

import os

# how many slots are there supposed to be?
slot_choices = ((x + 1, str(x + 1)) for x in xrange(3))

def generate_image_filename(instance, old_filename):
    extension = os.path.splitext(old_filename)[1]
    filename = instance.page.slug + extension
    return 'subhighlights/' + filename

class Subhighlight(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    slot = models.PositiveSmallIntegerField(choices=slot_choices)
    page = models.ForeignKey('pages.Page')
    image = models.ImageField(upload_to=generate_image_filename)
    
    def is_active(self):
        objs = Highlight.objects.filter(slot=self.slot).order_by('-created_on')
        return (objs.count() > 0 and objs.all()[0].id == self.id)
    
