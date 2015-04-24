from django.db import models
from django.contrib import admin

class Category(models.Model):
	name = models.CharField(max_length=75)

	def __unicode__(self):
		return self.name

class Meal(models.Model):
	category = models.ForeignKey(Category)
	name = models.CharField(max_length=75)
	price = models.CharField(max_length=75)
	image = models.ImageField(upload_to='')
	nutrition_info = models.CharField(max_length=225, null=True, blank=True)
	description = models.TextField()
	
	def __unicode__(self):
		return self.name

admin.site.register(Category)
admin.site.register(Meal)