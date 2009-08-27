from myproject.pages.models import Page
from myproject.news.models import Entry
from myproject.ads.models import Ad
from django.shortcuts import render_to_response

def home(request):
    news = Entry.objects.order_by('-created_on')[:3]
    ads = Ad.objects.order_by('?')[:3]
    
    return render_to_response('pages/home.html',
        {'news_entries': news, 'ads': ads})
