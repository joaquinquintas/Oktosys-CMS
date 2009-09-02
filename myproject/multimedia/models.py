from django.db import models
from django import forms

import gdata.youtube
import gdata.youtube.service
yt = gdata.youtube.service.YouTubeService()

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

class Photo(models.Model):
    title = models.CharField(max_length=255)
    added_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=generate_filename)
    
    def __unicode__(self):
        return self.title
    
class Video(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=255)
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
    
