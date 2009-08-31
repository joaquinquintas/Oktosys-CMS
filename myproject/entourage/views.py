from models import Rider, Race, Team
from models import RegistrationForm, ENewsletterForm

from myproject.shortcuts import render
from django.http import HttpResponseRedirect

import hashlib

def riders_new(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        
        return HttpResponseRedirect('/entourage/login')
    else:
        form = RegistrationForm()
    
    return render(request, 'entourage/riders_new.html', {'form': form})

def riders_home(request):
    # rider = 
    return riders_profile(request, rider_id)

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not username or not password:
            return HttpResponseRedirect('/entourage/login')
        
        try:
            rider = Rider.objects.get(username=username)
        except Rider.DoesNotExist:
            return HttpResponseRedirect('/entourage/login')
        
        if rider.password == hashlib.sha1(password).hexdigest():
            request.session['rider_id'] = rider.id
            return HttpResponseRedirect('/entourage')
        else:
            return HttpResponseRedirect('/entourage/login')
    else:
        return render(request, 'entourage/login.html')
