from myproject.sponsors_panel.models import Sponsor
from myproject.ads.models import Ad
from myproject.entourage.models import Rider
from myproject.shortcuts import get_rider, get_friends

def load_sponsors(request):
    return {'sponsors': Sponsor.objects.all()}

def load_ads(request):
    ads = Ad.objects.order_by('?')[:3]
    return {'ads': ads}

def load_session(request):
    return {'current_user': get_rider(request)}

def load_friends(request):
    all_friends = get_friends(request, get_rider(request))
    friends = []
    for fid in all_friends:
        try:
            friend = Rider.objects.get(facebook=str(fid))
        except Rider.DoesNotExist:
            pass
        else:
            friends.append(friend)
    
    return {'current_friends': all_friends,
            'current_reg_friends': friends}
