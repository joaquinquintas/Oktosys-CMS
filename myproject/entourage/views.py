from __future__ import with_statement # For with to work
from models import Rider, Race, Team
from models import RegistrationForm, ProfileUpdateForm, ENewsletterForm
from models import generate_filename

from myproject.shortcuts import render, get_rider, get_friends

from django.http import HttpResponseRedirect
from django.conf import settings

import hashlib

def home(request):
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
        form = ProfileUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # rider_info = form.save(commit=False)
            # 
            # rider.name_first = rider_info.name_first
            # rider.name_last = rider_info.name_last
            # rider.email = rider_info.email
            # rider.avatar = rider_info.avatar
            # rider.phone_main = rider_info.phone_main
            # rider.phone_mobile = rider_info.phone_mobile
            # rider.settings_updates_fb = rider_info.settings_updates_fb
            # rider.settings_updates_email = rider_info.settings_updates_email
            # rider.settings_updates_sms = rider_info.settings_updates_sms
            # rider.settings_fb_post = rider_info.settings_fb_post
            # rider.settings_profile_private = rider_info.settings_profile_private
            # 
            # rider.save()
        else:
            return render(request, 'entourage/edit_profile.html', {'form': form})
        return HttpResponseRedirect('/entourage/')
    else:
        form = ProfileUpdateForm({
            'name_first': rider.name_first,
            'name_last': rider.name_last,
            'email': rider.email,
            'avatar': rider.avatar,
            'phone_main': rider.phone_main,
            'phone_mobile': rider.phone_mobile,
            'settings_updates_fb': rider.settings_updates_fb,
            'settings_updates_email': rider.settings_updates_email,
            'settings_updates_sms': rider.settings_updates_sms,
            'settings_fb_post': rider.settings_fb_post,
            'settings_profile_private': rider.settings_profile_private,
        })
    
    return render(request, 'entourage/edit_profile.html', {'form': form})

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
