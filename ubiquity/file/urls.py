from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as authviews
from . import views

app_name = 'file'

urlpatterns = [
	url(r'^$', views.showfiles, name='list'),
	# url(r'^login/$', authviews.login,{'template_name':'acc/login.html'}, name='login'),
	# url(r'^logout/$', authviews.logout,{'template_name':'acc/logout.html'}, name='logout'),
	url(r'^socket/$', views.run_socket, name='socket'),
]