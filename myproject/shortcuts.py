from myproject.entourage.models import Rider, generate_filename

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect as redirect
from django.conf import settings

from facebook import djangofb as facebook

import urllib

def render(request, template, data={}):
    return render_to_response(template, data,
        context_instance=RequestContext(request))
 
def get_rider(request):
    rider = None
    
    # try standard login
    rider_id = request.session.get('rider_id')
    if rider_id:
        try:
            rider = Rider.objects.get(id=rider_id)
            return rider
        except Rider.DoesNotExist:
            pass

    # try facebook connect
    
    try:
        session_key = request.COOKIES.get('%s_session_key' % settings.FACEBOOK_API_KEY)
        uid = request.COOKIES.get('%s_user' % settings.FACEBOOK_API_KEY)
    except:
        pass
    else:
        if uid:
            try:
                rider = Rider.objects.get(facebook=uid)
            except Rider.DoesNotExist:
                fb = facebook.Facebook(settings.FACEBOOK_API_KEY,
                                       settings.FACEBOOK_SECRET_KEY)
                info = fb.users.getInfo([uid],
                    ['name', 'first_name', 'last_name', 'pic_big'])[0]
                name_first = info.get('first_name', '')
                name_last = info.get('last_name', '')
                if not name_first and not name_last:
                    name_first, name_last = info.get('name', '').rsplit(' ', 1)
                avatar_url = info.get('pic_big')
                
                if avatar_url:
                    avatar_contents = urllib.urlopen(avatar_url).read()
                rider = Rider(facebook=uid,
                    name_first=name_first,
                    name_last=name_last)
                avatar_fname = generate_filename(rider, 'avatar.jpg')
                open(settings.MEDIA_ROOT + avatar_fname, 'w').write(avatar_contents)
                rider.avatar = avatar_fname
                rider.save()
            finally:
                if rider:
                    return rider

def get_friends(request, rider):
    open('/home/spectrum/test', 'w').write('testing1')
    if rider.facebook:
        open('/home/spectrum/test', 'w').write('testing2')
        fb = facebook.Facebook(settings.FACEBOOK_API_KEY,
                               settings.FACEBOOK_SECRET_KEY)
        open('/home/spectrum/test', 'w').write('testing3')
        fb.session_key = request.COOKIES.get('%s_session_key' % settings.FACEBOOK_API_KEY)
        fb.uid = request.COOKIES.get('%s_user' % settings.FACEBOOK_API_KEY)
        open('/home/spectrum/test', 'w').write(rider.facebook)
        fids = fb.friends.get(uid=rider.facebook)
        open('/home/spectrum/test2', 'w').write(str(fids))
        open('/home/spectrum/test3', 'w').write(type(fids))
        open('/home/spectrum/test', 'w').write('testing5')
        friends = []
        open('/home/spectrum/test', 'w').write('testing6')
        for f in fb.users.getInfo(fids, ['name', 'pic_small']):
            open('/home/spectrum/test', 'w').write('testing7')
            friend = Rider.objects.get(facebook=f)
            open('/home/spectrum/test', 'w').write('testing8')
            if friend:
                open('/home/spectrum/test', 'w').write('testing9')
                friends.append(friend)
            open('/home/spectrum/test', 'w').write('testing10')

        open('/home/spectrum/test', 'w').write(str(friends))
        return friends
    else:
        return []
