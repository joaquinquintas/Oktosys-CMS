from myproject.news.models import Entry
from myproject.shortcuts import render
from django.shortcuts import get_object_or_404

def index(request):
    return render(request, 'news/index.html',
        {'entries': Entry.objects.all()})

def view(request, slug):
    entry = get_object_or_404(Entry, slug=slug)
    return render(request, 'news/entry.html', {'entry': entry})
