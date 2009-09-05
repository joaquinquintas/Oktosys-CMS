from myproject.news.models import Entry
from myproject.shortcuts import render

from django.shortcuts import get_object_or_404

import datetime

def index(request):
    today = datetime.datetime.today()
    this_month = today.month
    this_year = today.year
    
    month = request.GET.get('month', this_month)
    year = request.GET.get('year', this_year)
    
    try:
        month, year = int(month), int(year)
    except ValueError:
        month, year = this_month, this_year
    
    if month not in range(1, 13) or year not in range(10000):
        month, year = this_month, this_year
    
    entries = Entry.objects.filter(created_on__year=year,
                                   created_on__month=month)
    
    return render(request, 'news/index.html',
        {'entries': entries,
         'year_range': xrange(2009, year + 1),
         'current_year': year,
         'current_month': month})

def view(request, slug):
    entry = get_object_or_404(Entry, slug=slug)
    return render(request, 'news/entry.html', {'entry': entry})
