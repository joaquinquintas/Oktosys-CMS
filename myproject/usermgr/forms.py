from models import Rider
from django import forms

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Rider
    
    username = forms.CharField(label=u'Username', max_length=50)
	password = forms.CharField(label=u'Password', widget=forms.PasswordInput)
	name_first = forms.CharField(label=u'First name', max_length=150)
	name_last = forms.CharField(label=u'Last name', max_length=150)
	email = forms.EmailField(label=u'Email address')
	phone_main = forms.CharField(label=u'Telephone number', max_length=100)
	phone_mobile = forms.CharField(label=u'Mobile number', max_length=100)
	settings_updates_fb = forms.BooleanField(label=u'Receive updates via Facebook', widget=forms.CheckboxInput)
	settings_updates_email = forms.BooleanField(label=u'Receive updates via email', widget=forms.CheckboxInput)
	settings_updates_sms = forms.BooleanField(label=u'Receive updates via SMS', widget=forms.CheckboxInput)
	settings_fb_post = forms.BooleanField(label=u'Post your activities to Facebook', widget=forms.CheckboxInput)
	settings_share_profile = forms.BooleanField(label=u'Make your profile page private', widget=forms.CheckboxInput)

class ENewsletterForm(forms.Form):
	name = form.CharField(label=u'Name', max_length=100)
	email = forms.EmailField(label=u'Email address')
