from django.contrib import admin
from django.contrib.auth.models import User
from .models import *
# Register your models here.

class ImagesInline(admin.TabularInline ):
	model = Images
	extra=3
class FlexInline(admin.TabularInline ):
	model = Flex
	extra=1
class BlogsInline(admin.TabularInline ):
	model = BlogImages
	extra=1
class EventAdminView(admin.ModelAdmin):
	inlines = [ImagesInline, FlexInline]


class BlogsAdminView(admin.ModelAdmin):
	inlines = [BlogsInline]
	
admin.site.register(Events, EventAdminView)
admin.site.register(Blogs, BlogsAdminView)