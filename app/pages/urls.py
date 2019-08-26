from django.conf.urls import url
from . import views
from django.contrib import admin
app_name = 'pages'

admin.autodiscover() 
urlpatterns = [
    # url(r'^$', views.test, name='test'),  
    # url(r'^list/$', views.test_list, name='test_list'),  
    # url(r'^categories/$', views.categories, name='categories'), 
    url(r'^about/$', views.about, name='about'),  
    url(r'^sale/$', views.actions, name='actions'), 
    url(r'^sale/(?P<id>\d+)/$', views.action, name='action'),  
    url(r'^news/$', views.articles, name='articles'),   
    url(r'^news/(?P<id>\d+)/$', views.article, name='article'),  
    url(r'^contacts/$', views.contacts, name='contacts'),  
    url(r'^delivery/$', views.delivery, name='delivery'),  
    url(r'^faq/$', views.faq, name='faq'),  
    url(r'^garantee/$', views.garantee, name='garantee'),  
    url(r'^$', views.index, name='index'),  
    url(r'^404/$', views.notfound, name='notfound'),
]
