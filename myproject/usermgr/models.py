from django.db import models

class Rider(models.Model):
	name_first = models.CharField(max_length=150)
	name_last = models.CharField(max_length=150)
	email = models.EmailField(unique=True)
	phone_main = models.CharField(max_length=100)
	phone_mobile = models.CharField(max_length=100)
	
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	
	bike_make = models.CharField(max_length=255)
	bike_model = models.CharField(max_length=255)
	bike_link = models.URLField(verify_exists=True)
    
	settings_updates_fb = models.BooleanField(default=True)
	settings_updates_email = models.BooleanField(default=True)
	settings_updates_sms = models.BooleanField(default=True)
	settings_fb_post = models.BooleanField(default=True)
	settings_profile_private = models.BooleanField(default=False)

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
	user1 = models.ForeignKey('Rider')
	user2 = models.ForeignKey('Rider')
	user3 = models.ForeignKey('Rider')
	user4 = models.ForeignKey('Rider')
	status = models.BooleanField()
	counter = models.IntegerField()
