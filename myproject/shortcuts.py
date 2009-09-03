from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect as redirect
from django.core.files.uploadedfile import SimpleUploadedFile
import facebook.djangofb as fb
from myproject.entourage.models import Rider, generate_filename

def render(request, template, data={}):
    return render_to_response(template, data,
        context_instance=RequestContext(request))
 
def get_rider(request):
    # try standard login
    rider_id = request.session.get('rider_id')
    if rider_id:
        try:
            return Rider.objects.get(id=rider_id)
        except Rider.DoesNotExist:
            pass
    
    # try facebook connect
    
    try:
        fb.auth.getSession()
    except:
        pass
    else:
        if fb.uid:
            try:
                rider = Rider.objects.get(facebook=fb.uid)
            except Rider.DoesNotExist:
                info = facebook.users.getInfo([fb.uid],
                    ['first_name', 'last_name', 'pic_big'])[0]
                avatar_url = info.get('pic_big')
                if avatar_url:
                    avatar_contents = urllib.urlopen(avatar_url).read()
                rider = Rider(facebook=fb.uid,
                    name_first=info.get('first_name'),
                    name_last=info.get('last_name'))
                rider.avatar = generate_filename(rider, 'avatar.jpg')
                open(settings.MEDIA_URL + rider.avatar, 'w').write(avatar_contents)
                rider.save()
            else:
                return rider
