from django.conf.urls import url
from . import views
from django.contrib import admin
from django.conf import settings
app_name = 'lk'

# from django.contrib.auth.views import *
admin.autodiscover() 
urlpatterns = [
    # url(r'^$', views.test, name='test'),  
    url(r'^lk/$', views.lk, name='lk'),
    url(r'^orders/$', views.orders, name='orders'),  
    url(r'^orders/(?P<id>\d+)/$', views.cabinet3, name='cabinet3'),  
    url(r'^cabinet4/$', views.cabinet4, name='cabinet4'),  
    url(r'^cabinet5/$', views.cabinet5, name='cabinet5'),  
    url(r'^profile/$', views.profile, name='profile'),  
    url(r'^history/$', views.history, name='history'), 
    url(r'^reg/$', views.reg, name='reg'),  
    url(r'^password/$', views.password, name='password'),  
    url(r'^password2/$', views.password2, name='password2'),  
    url(r'^login/$', views.login, name='login'), 
    url(r'^logout/$', views.logout1, name='logout1'),
    url(r'^subscrible/$', views.formsubscribe, name='formsubscribe'),
    url(r'^call/$', views.callback, name='callback'),
    # url(r'^categories/$', views.categories, name='categories'), 
    
]