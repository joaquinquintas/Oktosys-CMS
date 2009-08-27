from myproject.pages.models import Page
from myproject.news.models import Entry
from myproject.ads.models import Ad

from myproject.shortcuts import render

def home(request):
    news = Entry.objects.order_by('-created_on')[:3]
    ads = Ad.objects.order_by('?')[:3]
    
    return render(request, 'pages/home.html',
        {'news_entries': news, 'ads': ads})
