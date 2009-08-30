from django.db import models

# Create your models here.

class Rider(models.Model):
	firstName = models.CharField(max_length=150)
	lastName = models.CharField(max_length=150)
	emailAdd = models.EmailField(unique=True)
	tel_main = models.CharField(max_length=100)
	tel_mobile = models.CharField(max_length=100)
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	bike_make = models.CharField(max_length=255)
	bike_model = models.CharField(max_length=255)
	bike_link = models.URLField(verify_exists=True)

class Rider_Settings(models.Model):
	rider_id = models.ForeignKey('Rider')
	recv_fbupdates = models.BooleanField()
	recv_emailupdates = models.BooleanField()
	recv_smsupdates = models.BooleanField()
	facebook_live = models.BooleanField()
	fb_ocbclink = models.BooleanField()
	privacy = models.BooleanField()

class Race_Profile(models.Model):
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
	rider_id = models.ForeignKey('Rider')
	registered = models.BooleanField()
	race_type = models.CharField(max_length=4, choices =RACE_TYPES)
	team_id = models.ForeignKey('Team')
	
class Team(models.Model):
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
	race_type = models.CharField(max_length=4, choices=TEAM_TYPES)
	user1_id = models.ForeignKey('Rider')
	user2_id = models.ForeignKey('Rider')
	user3_id = models.ForeignKey('Rider')
	user4_id = models.ForeignKey('Rider')
	team_status = models.BooleanField()
	counter = models.IntegerField()


