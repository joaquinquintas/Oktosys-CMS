from myproject.sponsors_panel.models import Sponsor

def load_sponsors(request):
    return {'sponsors': Sponsor.objects.all()}
