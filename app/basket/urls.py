from django.conf.urls import url
from . import views

app_name = 'cart'

urlpatterns = [
    url(r'^remove/(?P<product_id>\d+)/$', views.BasketRemove, name='BasketRemove'),
    url(r'^add/$', views.BasketAdd, name='BasketAdd'),
    url(r'^$', views.BasketDetail, name='BasketDetail'),

]