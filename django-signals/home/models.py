from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Artist(models.Model):
	name = models.ForeignKey(User)

	def __str__(self):
		if self.name:
			return str(self.name)


class Record(models.Model):
 	artist = models.ForeignKey(Artist)
 	name = models.CharField(max_length=20)
 	year = models.IntegerField()

 	def __str__(self):
 		return self.name

class Rating(models.Model):
 	record = models.ForeignKey(Record)
 	user = models.ForeignKey(User)
 	rating = models.IntegerField(default=0)
 	expected_rating = models.IntegerField(default=0)

 	def __str__(self):
 		return 'Record:{} and User:{}'.format(self.record,self.user)

@receiver(post_save, sender=Record)
def create_ratings_new_album(sender, instance, **kwargs):
	if kwargs['created']:
		users = User.objects.all()
		for user in users:
			Rating.objects.create(user=user, record=instance)

@receiver(post_save, sender=User)
def create_ratings_new_user(sender, instance, **kwargs):
	if kwargs['created']:
		records =Record.objects.all()
		for record in records:
			Rating.objects.create(user=instance, record=record)