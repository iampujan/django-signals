from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Artist(models.Model):
	name = models.ForeignKey(User)

	def __str__(self):
		return self.name


 class Record(models.Model):
 	artist = models.ForeignKey('Artist')
 	name = models.CharField()
 	year = models.IntergerField()

 	def __str__(self):
 		return self.name

 class Rating(models.Model):
 	record = models.ForeignKey('Record')
 	user = models.ForeignKey(User)
 	rating = models.IntergerField(default=0)
 	expected_rating = models.IntergerField(default=0)

 	def __str__(self):
 		return 'Record:{} and User:{}'.format(self.record,self.user)