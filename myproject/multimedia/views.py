from models import Photo

from myproject.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, InvalidPage, EmptyPage

def index(request):
    photos = Photo.objects.all()
    paginator = Paginator(photos, 45)
    
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        page = 1
    
    try:
        photos = paginator.page(page)
    except (EmptyPage, InvalidPage):
        photos = paginator.page(paginator.num_pages)
    
    return render(request, 'multimedia/index.html', {'photos': photos})

def photo_view(request, id):
    photo = get_object_or_404(Photo, id=id)
    return render(request, 'multimedia/view.html', {'photo': photo})
