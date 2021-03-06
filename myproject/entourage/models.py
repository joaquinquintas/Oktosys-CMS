from django.db import models
from django import forms
from django.conf import settings

from facebook import djangofb as facebook

import os
import time
import hashlib

def generate_filename(instance, old_filename):
    extension = os.path.splitext(old_filename)[1]
    filename = str(time.time()) + extension
    return 'riders/' + filename

class Rider(models.Model):
    name_first = models.CharField(max_length=150, blank=True)
    name_last = models.CharField(max_length=150, blank=True)
    
    def name(self):
        return "%s %s" % (self.name_first, self.name_last)
    
    email = models.EmailField(blank=True)
    phone_main = models.CharField(max_length=100, blank=True)
    phone_mobile = models.CharField(max_length=100, blank=True)
    
    username = models.CharField(max_length=50, blank=True)
    password = models.CharField(max_length=50, blank=True)
    
    avatar = models.ImageField(upload_to=generate_filename)
    
    team = models.ForeignKey('Team', null=True)
    
    settings_updates_fb = models.BooleanField(default=True)
    settings_updates_email = models.BooleanField(default=True)
    settings_updates_sms = models.BooleanField(default=True)
    settings_fb_post = models.BooleanField(default=True)
    settings_profile_private = models.BooleanField(default=False)
    
    # if the user logs in through Facebook, this is his uid
    facebook = models.CharField(max_length=255, blank=True)
    
    def get_race():
        pass
    
    def get_friends(self):
        if self.facebook:
            fb = facebook.Facebook(settings.FACEBOOK_API_KEY,
                                   settings.FACEBOOK_SECRET_KEY)
            fb.uid = self.facebook
            fids = fb.friends.get(uid=self.facebook)
            friends = []
            for f in fb.users.getInfo(fids, ['name', 'pic_small']):
                friend = Rider.objects.get(facebook=f)
                if friend:
                    friends.append(friend)
            
            return friends
        else:
            return []
    
    friends = property(get_friends)
    def unicode(self):
        return self.name
    def save(self):
        if not self.id:
            self.password = hashlib.sha1(self.password).hexdigest()
        
        if self.email and Rider.objects.filter(email=self.email).count() > 1:
            return False
        
        super(Rider, self).save()
    

RACE_TYPES = (
    ('I50', '50KM, INDIVIDUAL'),
    ('I40', '40KM, INDIVIDUAL'),
    ('I20', '20KM, INDIVIDUAL'),
    ('I5', '5KM, INDIVIDUAL'),
    ('IC', 'CRITERIUM, INDIVIDUAL'),
    ('ITR', 'TRICYCLE, INDIVIDUAL'),
    ('S50', '50KM, STUDENT'),
    ('S40', '40KM, STUDENT'),
    ('S20', '20KM, STUDENT'),
    ('S5', '5KM, STUDENT'),
    ('SC', 'CRITERIUM, STUDENT'),
    ('STR', 'TRICYCLE, STUDENT'),
    ('TC50', '50KM, TEAM, CORPORATE'),
    ('TC40', '40KM, TEAM, CORPORATE'),
    ('TC20', '20KM, TEAM, CORPORATE'),
    ('TC5', '5KM, TEAM, CORPORATE'),
    ('TCC', 'CRITERIUM, TEAM, CORPORATE'),
    ('TCTR', 'TRICYCLE, TEAM, CORPORATE'),
    ('TS50', '50KM, TEAM, SCHOOL'),
    ('TS40', '40KM, TEAM, SCHOOL'),
    ('TS20', '20KM, TEAM, SCHOOL'),
    ('TS5', '5KM, TEAM, SCHOOL'),
    ('TSC', 'CRITERIUM, TEAM, SCHOOL'),
    ('TSTR', 'TRICYCLE, TEAM, SCHOOL'),
    ('TO50', '50KM, TEAM, OTHER'),
    ('TO40', '40KM, TEAM, OTHER'),
    ('TO20', '20KM, TEAM, OTHER'),
    ('TO5', '5KM, TEAM, OTHER'),
    ('TOC', 'CRITERIUM, TEAM, OTHER'),
    ('TOTR', 'TRICYCLE, TEAM, OTHER'),
)

class Race(models.Model):
    rider = models.ForeignKey('Rider')
    registered = models.BooleanField()
    race_type = models.CharField(max_length=4, choices=RACE_TYPES)
    team_id = models.ForeignKey('Team')
    def __unicode__(self):
        return "%s %s %s" % (self.rider, self.Team, self.race_type)

TEAM_TYPES = (
    ('TC50', '50KM, TEAM, CORPORATE'),
    ('TC40', '40KM, TEAM, CORPORATE'),
    ('TC20', '20KM, TEAM, CORPORATE'),
    ('TC5', '5KM, TEAM, CORPORATE'),
    ('TCC', 'CRITERIUM, TEAM, CORPORATE'),
    ('TCTR', 'TRICYCLE, TEAM, CORPORATE'),
    ('TS50', '50KM, TEAM, SCHOOL'),
    ('TS40', '40KM, TEAM, SCHOOL'),
    ('TS20', '20KM, TEAM, SCHOOL'),
    ('TS5', '5KM, TEAM, SCHOOL'),
    ('TSC', 'CRITERIUM, TEAM, SCHOOL'),
    ('TSTR', 'TRICYCLE, TEAM, SCHOOL'),
    ('TO50', '50KM, TEAM, OTHER'),
    ('TO40', '40KM, TEAM, OTHER'),
    ('TO20', '20KM, TEAM, OTHER'),
    ('TO5', '5KM, TEAM, OTHER'),
    ('TOC', 'CRITERIUM, TEAM, OTHER'),
    ('TOTR', 'TRICYCLE, TEAM, OTHER'),
)

class Team(models.Model):
    race_type = models.CharField(max_length=4, choices=TEAM_TYPES)
    status = models.BooleanField()
    counter = models.IntegerField()
    def __unicode__(self):
        return "Team %s %s %s %s" % (self.id, self.race_type,self.status, self.counter)

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Rider
        fields = (
            'name_first', 'name_last',
            'email',
            'username', 'password',
            'avatar',
            'phone_main', 'phone_mobile',
            'settings_updates_fb',
            'settings_updates_email',
            'settings_updates_sms',
            'settings_fb_post',
            'settings_profile_private',
        )
    
    username = forms.CharField(label=u'Username', max_length=50)
    password = forms.CharField(label=u'Password', widget=forms.PasswordInput)
    name_first = forms.CharField(label=u'First name', max_length=150)
    name_last = forms.CharField(label=u'Last name', max_length=150)
    email = forms.EmailField(label=u'Email address')
    avatar = forms.ImageField(label=u'Avatar', required=False)
    phone_main = forms.CharField(label=u'Telephone number', max_length=100, required=False)
    phone_mobile = forms.CharField(label=u'Mobile number', max_length=100, required=False)
    settings_updates_fb = forms.BooleanField(label=u'Receive updates via Facebook', widget=forms.CheckboxInput, initial=True, required=False)
    settings_updates_email = forms.BooleanField(label=u'Receive updates via email', widget=forms.CheckboxInput, initial=True, required=False)
    settings_updates_sms = forms.BooleanField(label=u'Receive updates via SMS', widget=forms.CheckboxInput, initial=True, required=False)
    settings_fb_post = forms.BooleanField(label=u'Post your activities to Facebook', widget=forms.CheckboxInput, initial=True, required=False)
    settings_profile_private = forms.BooleanField(label=u'Make your profile page private', widget=forms.CheckboxInput, initial=False, required=False)

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Rider
        fields = (
            'name_first', 'name_last',
            'email',
            'avatar',
            'phone_main', 'phone_mobile',
            'settings_updates_fb',
            'settings_updates_email',
            'settings_updates_sms',
            'settings_fb_post',
            'settings_profile_private',
        )

    name_first = forms.CharField(label=u'First name', max_length=150)
    name_last = forms.CharField(label=u'Last name', max_length=150)
    email = forms.EmailField(label=u'Email address')
    avatar = forms.ImageField(label=u'Avatar', required=False)
    phone_main = forms.CharField(label=u'Telephone number', max_length=100, required=False)
    phone_mobile = forms.CharField(label=u'Mobile number', max_length=100, required=False)
    settings_updates_fb = forms.BooleanField(label=u'Receive updates via Facebook', widget=forms.CheckboxInput, initial=True, required=False)
    settings_updates_email = forms.BooleanField(label=u'Receive updates via email', widget=forms.CheckboxInput, initial=True, required=False)
    settings_updates_sms = forms.BooleanField(label=u'Receive updates via SMS', widget=forms.CheckboxInput, initial=True, required=False)
    settings_fb_post = forms.BooleanField(label=u'Post your activities to Facebook', widget=forms.CheckboxInput, initial=True, required=False)
    settings_profile_private = forms.BooleanField(label=u'Make your profile page private', widget=forms.CheckboxInput, initial=False, required=False)

    