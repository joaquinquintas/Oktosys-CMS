from django.template import RequestContext
from django.shortcuts import render_to_response
from myproject.entourage import models

def render(request, template, data={}):
    return render_to_response(template, data,
        context_instance=RequestContext(request))

def auth(request):
    rider_id = request.session['rider_id']
    if not rider_id:
        return False
    else:
        try:
            return models.Rider(id=rider_id)
            return rider
        except Rider.DoesNotExist:
            return False
