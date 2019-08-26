from django.conf.urls import url
from . import views
from django.contrib import admin
app_name = 'catalog'

admin.autodiscover() 
urlpatterns = [
    url(r'^catalog/$', views.categories, name='categories'),
    url(r'^catalog/(?P<hierarchy>.+)/(?P<pk>\d+)', views.product_detail, name='product_detail'),
    url(r'^catalog/(?P<hierarchy>.+)/', views.product_list, name='product_list'),
    url(r'^find/$', views.find, name='find'),
]