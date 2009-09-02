from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect as redirect
from myproject.entourage.models import Rider

def render(request, template, data={}):
    return render_to_response(template, data,
        context_instance=RequestContext(request))

def auth(request):
    rider_id = request.session.get('rider_id')
    if not rider_id:
        return False
    else:
        try:
            return Rider.objects.get(id=rider_id)
        except Rider.DoesNotExist:
            return False
