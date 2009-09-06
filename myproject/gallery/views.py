from models import Photo
from models import PhotoForm

from myproject.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

def index(request):
    return render(request, 'gallery/index.html',
        {'photos': Photo.objects.all()})

def photos_view(request, id):
    photo = get_object_or_404(Photo, id=id)
    return render(request, 'gallery/view.html', {'photo': photo})

def photos_new(request):
    rider = get_rider(request)
    if not rider:
        return redirect('/entourage/login')
    
    if request.method == 'POST':
        form = PhotoForm(request.POST)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.added_by = rider
            photo.save()
            form.save_m2m()
            
            return redirect('/gallery/%s' % photo.id)
    else:
        form = PhotoForm()
    
    return render(request, 'gallery/new.html', {'form': form})
