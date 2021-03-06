# Create your views here.
from myproject.enewsletter.models import EnewsForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

def subscribe(request):
	if request.method == 'POST':
		form = EnewsForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/enewsletter/subscribed/')
		else: 
			return HttpResponseRedirect('/enewsletter/')
	else:
		form = EnewsForm()

	return render_to_response('enewsletter/subscribe.html', 
		  { 'form': form, })


def subscribed(request):
	return render_to_response('enewsletter/subscribed.html')