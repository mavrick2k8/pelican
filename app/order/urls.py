from django.conf.urls import url
from . import views
from django.contrib import admin
app_name = 'order'

admin.autodiscover() 
urlpatterns = [
    # url(r'^$', views.test, name='test'),  
    # url(r'^list/$', views.test_list, name='test_list'),  
    url(r'^(?P<pk>\d+)/success$', views.order1, name='order1'),
    # url(r'^success/$', views.order1, name='order1'),  
    url(r'^order/$', views.order, name='order'),  
    url(r'^check/pay/$', views.check_paiment, name='check_paiment'),  
    # url(r'^order2/$', views.order2, name='order2'),  
    # url(r'^order3/$', views.order3, name='order3'),  
    # url(r'^order4/$', views.order4, name='order4'),  
    # url(r'^order5/$', views.order5, name='order5'),  
    # url(r'^categories/$', views.categories, name='categories'), 
]