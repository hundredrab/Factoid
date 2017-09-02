from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as authviews
from . import views

app_name = 'profile'

urlpatterns = [
	url(r'^$', views.profile, name='home'),
	url(r'^login/$', authviews.login,{'template_name':'acc/login.html'}, name='login'),
	url(r'^logout/$', authviews.logout,{'template_name':'acc/logout.html'}, name='logout'),
	url(r'^register/$', views.register, name='register'),
]