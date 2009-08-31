from myproject.pages.models import Page
from myproject.news.models import Entry

from myproject.shortcuts import render
from django.shortcuts import get_object_or_404

def home(request):
    news = Entry.objects.order_by('-created_on')[:3]
    
    return render(request, 'pages/home.html', {'news_entries': news})

def serve(request, slug):
    page = get_object_or_404(Page, slug=slug)
    
    return render(request, 'pages/serve.html', {'page': page})
