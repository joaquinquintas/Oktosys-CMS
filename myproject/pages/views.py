from myproject.pages.models import Page
from myproject.news.models import Entry
from myproject.subhighlights.models import Subhighlight as Shs
from myproject.shortcuts import render
from django.shortcuts import get_object_or_404

def home(request):
    news = Entry.objects.order_by('-created_on')[:3]
    shs = Shs.objects.all()
    return render(request, 'pages/home.html', 
                {'news_entries': news,
                 'shs': shs})

def serve(request, slug):
    page = get_object_or_404(Page, slug=slug)
    
    breadcrumbs = page.breadcrumbs()
    breadcrumbs = " &raquo; ".join(('<a href="/pages/%s">%s</a>' % x for x in breadcrumbs))
    
    return render(request, 'pages/serve.html', {'page': page,
        'breadcrumbs': breadcrumbs})
