from django.db import models

import datetime

year = datetime.datetime.now().year
photo_years = xrange(year, year - 5, -1)

photo_categories = (
    'The Challenge - 40km',
    # ...
)

class Photo(models.Model):
    title = models.CharField(max_length=255)
    added_on = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey('users.User')
    category = models.CharField(max_length=255, choices=photo_categories)
    year = models.PositiveIntegerField(choices=photo_years)
    
    def __unicode__(self):
        return self.title
    
