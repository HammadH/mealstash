from django.views.generic import View
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.conf import settings

from emails.models import Subscriber
from meals.models import *



class HomePage(View):
	def get(self, request, *args, **kwargs):
		customers = 154 + Subscriber.objects.all().count()
		all_meals = Meal.objects.all()
		meals = Meal.objects.filter(category__name='Running')
		juices = Meal.objects.filter(category__name='Juices')
		bodybuilding_meals = Meal.objects.filter(category__name='Bodybuilding')
		return render_to_response('index.html', {'customers': customers, 'meals_1':meals[:12], 'meals_2':meals[12:],'juices':juices, 
			'meals_copy': all_meals, 'meals_3':bodybuilding_meals})

	def post(self, request, *args, **kwargs):
		try:
			Subscriber.objects.create(email=request.POST.get('email'))
			return HttpResponse(status=200)
		except Exception, e:
			print e
			return	HttpResponse(status=200)
