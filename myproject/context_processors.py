from myproject.sponsors_panel.models import Sponsor
from myproject.ads.models import Ad

def load_sponsors(request):
    return {'sponsors': Sponsor.objects.all()}

def load_ads(request):
    ads = Ad.objects.order_by('?')[:3]
    return {'ads': ads}
