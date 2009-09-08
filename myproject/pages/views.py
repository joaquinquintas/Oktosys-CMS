from myproject.pages.models import Page, get_slug_and_relative_path
from myproject.news.models import Entry
from myproject.subhighlights.models import Subhighlight as Shs
from myproject.shortcuts import render
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
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

def serve(request, path=None):
    current_page = False
    template_name = "pages/serve.html"

    if path is None:
        slug, path = get_slug_and_relative_path(request.path)
    if path:
        current_page = Page.objects.from_path(path)
    elif pages:
        current_page = Page.objects.order_by("tree_id")[0]
  
    current_page = get_object_or_404(Page, slug=slug)
    context = {
          'path': path,
          'current_page': current_page,   
      }
    return render_to_response(template_name, context,context_instance=RequestContext(request))
