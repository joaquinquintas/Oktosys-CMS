# Create your views here.
from myproject.enewsletter.models import EnewsForm
from django.http import HttpResponseRedirect

def subscribe(request):
	if request.method == 'POST':
		form = EnewsForm(request.POST)
		if form.is_valid:
			form.name = form.cleaned_data['name']
			form.email_add = form.cleaned_data['email_add']
			form.save()
			return HttpResponseRedirect('/subscribed/')
		else:
			form = EnewsForm()



