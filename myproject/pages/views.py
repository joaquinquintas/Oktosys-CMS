from myproject.pages.models import Page
from myproject.news.models import Entry
from myproject.subhighlights.models import Subhighlight as Shs
from myproject.shortcuts import render

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

def home(request):
    if request.session.get('first_fb_login'):
        request.session['first_fb_login'] = False
        del request.session['first_fb_login']
        return HttpResponseRedirect('/entourage/edit_profile')
    
    news = Entry.objects.order_by('-created_on')[:3]
    shs = Shs.objects.all()
    return render(request, 'pages/home.html', 
                {'news_entries': news,
                 'shs': shs,
                 'show_fb_stream': True})

def serve(request, slug):
    page = get_object_or_404(Page, slug=slug)
    
    return render(request, 'pages/serve.html', {'page': page,
        'breadcrumbs': page.breadcrumbs(),
        'show_fb_stream': page.show_fb_stream})
