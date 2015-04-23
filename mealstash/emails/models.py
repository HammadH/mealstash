from django.db import models
from django.contrib import admin

class Subscriber(models.Model):
	email = models.EmailField(unique=False, null=True)

	def __unicode__(self):
		return self.email

admin.site.register(Subscriber)
