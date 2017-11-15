# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
from django.db import models

# Create your models here.

class RestaurantLocation(models.Model):
	name 			= models.CharField(max_length=150)
	location 		= models.CharField(max_length=150, null = True, blank = True)
	category 		= models.CharField(max_length=150, null = True, blank = True)
	timestamp		= models.DateTimeField( auto_now_add = True)
	updated 		= models.DateTimeField(auto_now = True)
	#my_date_field 	= models.DateTimeField(auto_now = False, auto_now_add = False)
	slug			= models.SlugField(null = True, blank = True)

	def __str__(self):
		return self.name

	@property
	def title (self):
		return self.name	


def rl_pre_save_receiver(sender, instance, *args, **kwargs): #before saving to the database, this method is called
#instance is the object that we are going to store in the database
	print "saving..."
	print instance.timestamp
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)


def rl_post_save_receiver(sender, instance, created,*args, **kwargs):#after saving to the database, this method is called
	print "saved"
	print instance.timestamp
	
pre_save.connect(rl_pre_save_receiver, sender=RestaurantLocation)
post_save.connect(rl_post_save_receiver, sender=RestaurantLocation)