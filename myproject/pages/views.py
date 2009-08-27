from myproject.pages.models import *
from myproject.news.models import *
from django.shortcuts import render_to_response

def home(request):
    news = Entry.objects.order_by('-created_on')[:3]
    
    return render_to_response('pages/home.html', {'news_entries': news})
