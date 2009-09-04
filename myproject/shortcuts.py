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
                    ['first_name', 'last_name', 'pic_big'])[0]
                avatar_url = info.get('pic_big')
                if avatar_url:
                    avatar_contents = urllib.urlopen(avatar_url).read()
                rider = Rider(facebook=uid,
                    name_first=info.get('first_name'),
                    name_last=info.get('last_name'))
                rider.avatar = generate_filename(rider, 'avatar.jpg')
                open(settings.MEDIA_URL + rider.avatar, 'w').write(avatar_contents)
                rider.save()
            finally:
                if rider:
                    return rider
