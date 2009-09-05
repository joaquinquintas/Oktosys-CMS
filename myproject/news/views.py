from myproject.news.models import Entry
from myproject.shortcuts import render

from django.shortcuts import get_object_or_404

import datetime

def index(request, month=None, year=None):
    try:
        month, year = int(month), int(year)
    except ValueError:
        month, year = False, False
    
    if month not in range(1, 13) or year not in range(9999):
        today = datetime.datetime.today()
        month = today.month
        year = today.year
    
    entries = Entry.objects.filter(created_on__year=year,
                                   created_on__month=month)
    
    return render(request, 'news/index.html',
        {'entries': entries, 'year_range': xrange(2009, year + 1)})

def view(request, slug):
    entry = get_object_or_404(Entry, slug=slug)
    return render(request, 'news/entry.html', {'entry': entry})
