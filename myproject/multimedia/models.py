from django.db import models

import datetime

class Photo(models.Model):
    title = models.CharField(max_length=255)
    added_on = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey('entourage.Rider')
    
    tag = models.ManyToManyField('Tag')
    
    def __unicode__(self):
        return self.title
    

class Tag(models.Model):
    name = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.name
    
