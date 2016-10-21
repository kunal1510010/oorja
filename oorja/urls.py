from django.conf.urls import url

from . import views

app_name = 'oorja'

urlpatterns = [
	#url(r'^adminPage/$', views.AdminIndexView.as_view(), name='adminPage'),
	url(r'^Gallery/(?P<e_id>\d+)/$', views.GalleryView.as_view(), name='Gallery'),
	url(r'^Blogs/$', views.BlogView.as_view(), name='Blogs'),
	url(r'^$', views.IndexView.as_view(), name='Index'),
	url(r'^events/$', views.EventsView.as_view(), name='Events'),
]