from models import Rider, Race, Team
from models import RegistrationForm, ENewsletterForm

from myproject.shortcuts import render, auth
from django.http import HttpResponseRedirect

import hashlib

def home(request):
    rider = auth(request)
    if not rider:
        return HttpResponseRedirect('/entourage/login')
    return profile(request, rider.id)

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            render(request, 'entourage/signup.html', {'form': form})
        return HttpResponseRedirect('/entourage/login')
    else:
        form = RegistrationForm()

    return render(request, 'entourage/signup.html', {'form': form})

def profile(request, rider_id):
    try:
        rider = Rider.objects.get(id=rider_id)
    except Rider.DoesNotExist:
        return HttpResponseRedirect('/')
    
    if (rider.settings_profile_private
    and request.session['rider_id'] != rider.id):
        return render(request, 'entourage/profile.html', {
            'error': 'profile_private'})
    
    return render(request, 'entourage/profile.html', {'rider': rider})

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
