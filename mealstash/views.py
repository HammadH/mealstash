from django.views.generic import View
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.conf import settings

from emails.models import Subscriber



class HomePage(View):
	def get(self, request, *args, **kwargs):
		customers = 154 + Subscriber.objects.all().count()
		return render_to_response('index.html', {'customers': customers})

	def post(self, request, *args, **kwargs):
		try:
			Subscriber.objects.create(email=request.POST.get('email'))
			return HttpResponse(status=200)
		except Exception, e:
			print e
			return	HttpResponse(status=200)
