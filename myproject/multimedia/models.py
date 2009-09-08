from django.db import models
from django import forms

import gdata.youtube
import gdata.youtube.service
yt = gdata.youtube.service.YouTubeService()
from django.contrib.auth.models import User
from imagekit.models import ImageModel
from datetime import datetime

from tagging.fields import TagField


from django.conf import settings
yt.developer_key = settings.YOUTUBE_KEY

yt_regex = r'^((?:http://)?(?:\w+\.)?youtube\.com/(?:(?:v/)|(?:(?:watch(?:\.php)?)?\?(?:.+&)?v=)))?([0-9A-Za-z_-]+)(?(1).+)?$'

import os
import time
import re

def generate_filename(instance, old_filename):
    extension = os.path.splitext(old_filename)[1]
    filename = str(time.time()) + extension
    return 'multimedia/' + filename

class Photo(ImageModel):
    crop_horz_choices = (
       (0, 'left'),
       (1, 'center'),
       (2, 'right'),
     )
    crop_vert_choices = (
      (0, 'top'),
      (1, 'center'),
      (2, 'bottom'),
    )
    category_choices = (
      (0, 'The Super Challenge - 50Km'),
      (1, 'The Challenge - 40Km'),
      (2, 'The Community Ride - 20Km'),
      (3, 'Mighty Savers Kids Ride - 5Km'),
      (4, 'Criterium Events'),
      )
    year_choices = ((0,'2007'), (1,'2008'), (2,'2009'), (3,'2010'),)
    image = models.ImageField(upload_to=generate_filename)
    view_count = models.IntegerField(default=0)
    crop_horz = models.PositiveIntegerField('crop horizontal',
                              choices=crop_horz_choices,default=1)
    crop_vert = models.PositiveIntegerField('crop vertical',
                             choices=crop_vert_choices, default=1)
    title = models.CharField(max_length=255)
    title_slug = models.SlugField('slug')
    caption = models.TextField('caption', blank=True)
    date_added = models.DateTimeField('date added', default=datetime.now, editable=False)
    member = models.ForeignKey(User, related_name="added_photos", blank=True, null=True)
    category = models.CharField(max_length=255, choices=category_choices, default=1)
    year = models.CharField(max_length=255, choices=year_choices, default=2)
 #   added_on = models.DateTimeField(auto_now_add=True)
    tags = TagField()
    
    class IKOptions:
        spec_module = 'myproject.multimedia.specs'
        save_count_as = 'view_count'
        cache_dir = 'photos'
        
    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        return ("photo_details", [self.pk])
    get_absolute_url = models.permalink(get_absolute_url)
    
class Video(Photo):
    url = models.URLField()
    embed_url = models.CharField(max_length=255)
    embed_type = models.CharField(max_length=255)
    
    def save(self):
        try:
            video_id = re.compile('.*\?v\=([^\\\/&]+)').match(self.url).groups()[0]
            video = yt.GetYouTubeVideoEntry(video_id=video_id)
            
            self.title = video.media.title.text
            self.embed_url = video.media.content[0].url
            self.embed_type = video.media.content[0].type
            
            super(Video, self).save()
        except:
            pass
    
    def __unicode__(self):
        return self.url
    
