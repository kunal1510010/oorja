from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blogs(models.Model):
	title = models.CharField(max_length = 100, null = True , blank = True)
	content = models.TextField()
	pubDate = models.DateTimeField('date published', auto_now_add = True)
	link = models.URLField(null = True , blank = True) 

def content_file_name(instance, filename):
	ext = filename.split('.')[-1]
	filename = "%s.%s" % (instance.event.id, ext)
	return '/'.join(['oorja/static/oorja/event_images', filename])

def blog_file_name(instance, filename):
	ext = filename.split('.')[-1]
	filename = "%s.%s" % (instance.blog.id, ext)
	return '/'.join(['oorja/static/oorja/blog_images', filename])



class Events(models.Model):
	eventName = models.CharField(max_length = 20)
	eventDate = models.DateField(null = True , blank = True)
	eventRegDate = models.DateField(null = True , blank = True)
	eventContent = models.TextField(null = True , blank = True)


class Images(models.Model):
	def __str__(self):
		return str(self.image).split('/')[-1]
	event = models.ForeignKey(Events)
	image = models.ImageField(upload_to=content_file_name,default='event_images/'+str(id)+'.jpg')


class BlogImages(models.Model):
	def __str__(self):
		return str(self.image).split('/')[-1]
	blog = models.ForeignKey(Blogs)
	image = models.ImageField(upload_to=blog_file_name,default='blog_images/'+str(id)+'.jpg')

class Flex(models.Model):
	def __str__(self):
		return str(self.image).split('/')[-1]
	event = models.ForeignKey(Events)
	image = models.ImageField(upload_to=content_file_name,default='event_images/'+str(id)+'.jpg')
