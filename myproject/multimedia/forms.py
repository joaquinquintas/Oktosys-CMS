from django import forms
from datetime import datetime
from myproject.multimedia.models import photo

class PhotoUploadForm(forms.ModelForm):
    
    class Meta:
        model = Photo
        exclude = ('member','title_slug','effect','crop_from')
        
    def __init__(self, user=None, *args, **kwargs):
        self.user = user
        super(PhotoUploadForm, self).__init__(*args, **kwargs)