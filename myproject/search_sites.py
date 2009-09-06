from haystack import site
from myproject.pages.models import Page
from myproject.multimedia.models import Photo, Video
from myproject.entourage.models import Rider, Race, Team

site.register(Page)
site.register(Photo)
site.register(Video)
site.register(Rider)
site.register(Race)
site.register(Team)
