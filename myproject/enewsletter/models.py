from django.db import models
from django.forms import ModelForm

# Create your models here.

class EnewsSubscriber(models.Model):
	name = models.CharField('Name',max_length=100)
	email_add = models.EmailField('Email Address',max_length=100, unique=True)

	def __unicode__(self):
		return self.name

class EnewsForm(ModelForm):
	class Meta:
		model = EnewsSubscriber
