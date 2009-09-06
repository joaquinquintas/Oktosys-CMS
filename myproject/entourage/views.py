from __future__ import with_statement # For with to work
from models import Rider, Race, Team
from models import RegistrationForm, ENewsletterForm
from models import generate_filename

from myproject.shortcuts import render, get_rider
from django.http import HttpResponseRedirect
from django.conf import settings
import hashlib

def home(request):
    rider = get_rider(request)
    if not rider:
        return HttpResponseRedirect('/entourage/login')
    open('/home/spectrum/test', 'w').write(str((rider.name(), rider.id, rider.facebook)))
    return profile(request, rider.id)

def signup(request):
    rider = get_rider(request)
    
    if rider:
        return HttpResponseRedirect('/entourage/')
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            rider = form.save(commit=False)
            
            if not rider.avatar:
                fname = generate_filename(rider, 'default.jpg')
                rider.avatar = fname
                default = settings.MEDIA_ROOT + 'riders/default.jpg'
                with open(default) as default:
                    with open(fname, 'w') as f:
                        f.write(default.read())
            
            rider.save()
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
        return HttpResponseRedirect('/test')
    
    if (rider.settings_profile_private
    and request.session.get('rider_id') != rider.id):
        return render(request, 'entourage/profile.html', {
            'error': 'profile_private'})
    
    return render(request, 'entourage/profile.html', {'rider': rider})

def login(request):
    rider = get_rider(request)
    
    if rider:
        return HttpResponseRedirect('/entourage/')
    
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

def logout(request):
    rider = get_rider(request)
    
    if rider:
        request.session['rider_id'] = False
        del request.session['rider_id']
    
    return HttpResponseRedirect('/')
