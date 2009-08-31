from models import Rider, Race, Team
from models import RegistrationForm, ENewsletterForm

from myproject.shortcuts import render

def riders_new(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RegistrationForm()
    
    return render(request, 'entourage/riders_new.html', {'form': form})
