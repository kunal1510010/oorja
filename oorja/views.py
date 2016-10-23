from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone, dateparse
from datetime import datetime, timedelta
from django.contrib.auth import authenticate
from django.db.models import Q

from .models import *
from .forms import *

# Create your views here.

class GalleryView(generic.TemplateView):
	template_name = 'oorja/collections.html'
	def get(self, request, e_id,*args, **kwargs):
		try:
			today = datetime.today()
			last_five = Events.objects.filter(eventDate__lte = today).order_by('-eventDate')[:5]
			if int(e_id) == 1000000:
				return HttpResponseRedirect("/Gallery/" + str(last_five[0].id))
			else:
				images = Events.objects.get(pk=int(e_id)).images_set.all()
			context = {'Events':last_five, 'Images':images}
			return render(request, self.template_name, context)
		except:
			return HttpResponseRedirect("/" )



class BlogView(generic.TemplateView):
	template_name = 'oorja/Blog.html'
	def get(self, request, *args, **kwargs):
		blogs = Blogs.objects.all()
		context = {'Blogs':blogs}

		return render(request, self.template_name, context)


class IndexView(generic.TemplateView):
	template_name = 'oorja/index.html'
	def get(self, request, *args, **kwargs):
		return render(request, self.template_name)
class AboutView(generic.TemplateView):
	template_name = 'oorja/about.html'
	def get(self, request, *args, **kwargs):
		return render(request, self.template_name)

class EventsView(generic.TemplateView):
	template_name = 'oorja/events.html'
	def get(self, request, *args, **kwargs):
		events = Events.objects.all()
		context = {'Events':events}
		return render(request, self.template_name, context)
