from django.template import RequestContext
from django.shortcuts import render_to_response

def render(request, template, data):
    return render_to_response(template, data,
        context_instance=RequestContext(request))
