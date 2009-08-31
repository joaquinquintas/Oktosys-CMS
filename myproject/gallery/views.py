from myproject.gallery.models import Photo

from myproject.shortcuts import render
from django.shortcuts import get_object_or_404

def index(request):
    return render(request, 'gallery/index.html',
        {'photos': Photo.objects.all()})

def photos_view(request, id):
    photo = get_object_or_404(Photo, id=id)
    return render(request, 'gallery/view.html', {'photo': photo})
