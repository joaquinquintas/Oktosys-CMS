#Organic registration
from django import forms

class RegistrationForm(models.Model):
	username = forms.CharField(label=u'Username', max_length=50)
	password = forms.CharField(label=u'Password', widget=forms.PasswordInput)
	email = forms.EmailField(label=u'Email address')
	firstName = forms.CharField(label=u'First Name', max_length=100)
	lastName = forms.CharField(label=u'Last Name', max_length=100)
	tel_main = forms.CharField(label=u'Telephone', max_length=100)
	tel_mobile = forms.CharField(label=u'Mobile', max_length=100)
	rcv_fbupdates = forms.BooleanField(label=u'Receive Facebook updates', widget=forms.CheckboxInput)
	rcv_smsupdates = forms.BooleanField(label=u'Receive SMS updates', widget=forms.CheckboxInput)
	rcv_emailupdates = forms.BooleanField(label=u'Receive email updates', widget=forms.CheckboxInput)
	
class EnewsletterForm(models.Model):
	name = form.CharField(label=u'Name', max_length=100)
	email = forms.EmailField(label=u'Email Addresss')


	
	
	


