from django.db import models
from django import forms

class Photo(models.Model):
    title = models.CharField(max_length=255)
    added_on = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey('entourage.Rider')
    
    tag = models.ManyToManyField('Tag')
    
    def __unicode__(self):
        return self.title
    

class PhotoForm(forms.modelForm):
    class Meta:
        model = Photo
        fields = ('title', 'tag')
    

class Tag(models.Model):
    name = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.name
    
