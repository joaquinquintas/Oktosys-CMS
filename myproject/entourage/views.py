from __future__ import with_statement # For with to work
from models import Rider, Race, Team
from models import RegistrationForm, ProfileUpdateForm
from models import generate_filename

from myproject.shortcuts import render, get_rider, get_friends

from django.http import HttpResponseRedirect
from django.conf import settings

import hashlib

def home(request):
    if request.session.get('first_fb_login'):
        request.session['first_fb_login'] = False
        del request.session['first_fb_login']
        return HttpResponseRedirect('/entourage/edit_profile')
    
    rider = get_rider(request)
    if not rider:
        return HttpResponseRedirect('/entourage/login')
    return profile(request, rider.id)

def profile(request, rider_id):
    try:
        rider = Rider.objects.get(id=rider_id)
    except Rider.DoesNotExist:
        return HttpResponseRedirect('/')

    if (rider.settings_profile_private
    and request.session.get('rider_id') != rider.id):
        return render(request, 'entourage/profile.html', {
            'error': 'profile_private'})

    all_friends = get_friends(request, rider)

    friends = []
    for fid in all_friends:
        try:
            friend = Rider.objects.get(facebook=str(fid))
        except Rider.DoesNotExist:
            pass
        else:
            friends.append(friend)

    return render(request, 'entourage/profile.html', {'rider': rider,
        'friends': friends})

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
            return render(request, 'entourage/signup.html', {'form': form})
        return HttpResponseRedirect('/entourage/login')
    else:
        form = RegistrationForm()

    return render(request, 'entourage/signup.html', {'form': form})

def profile_edit(request):
    rider = get_rider(request)
    
    if not rider:
        return HttpResponseRedirect('/entourage/login')
    
    if request.method == 'POST':
        data = request.POST
        open('/home/spectrum/test', 'a').write(str(data))
        rider.name_first = data.get('name_first')
        rider.name_last = data.get('name_last')
        rider.email = data.get('email')
        rider.phone_main = data.get('phone_main')
        rider.phone_mobile = data.get('phone_mobile')
        rider.settings_updates_fb = (data.get('settings_updates_fb') == 'on')
        rider.settings_updates_email = (data.get('settings_updates_email') == 'on')
        rider.settings_updates_sms = (data.get('settings_updates_sms') == 'on')
        rider.settings_fb_post = (data.get('settings_fb_post') == 'on')
        rider.settings_profile_private = (data.get('settings_profile_private') == 'on')
        
        avatar = request.FILES.get('avatar')
        if avatar:
            def handle_upload(f):
                destination = open(settings.MEDIA_ROOT + rider.avatar.name, 'wb+')
                for chunk in f.chunks():
                    destination.write(chunk)
                destination.close()
            
            handle_upload(avatar)
        
        try:
            rider.save()
            return HttpResponseRedirect('/entourage')
        except:
            return render(request, 'entourage/edit_profile.html', {
                'rider': rider})
    else:
        return render(request, 'entourage/edit_profile.html', {
            'rider': rider})

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
