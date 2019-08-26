"""vsempostel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve 
from django.conf.urls import url, include
from django.conf.urls import handler400, handler403, handler404, handler500
from django.contrib.auth.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('catalog.urls', namespace='catalog')),
    # url(r'^', include('basket.urls', namespace='basket')),
    url(r'^', include('lk.urls', namespace='lk')),
    url(r'^', include('order.urls', namespace='order')),
    url(r'^', include('pages.urls', namespace='pages')),
    url(r'^basket/', include('basket.urls', namespace='basket')),

    url(r'^user/password/reset/$', password_reset, {'post_reset_redirect' : '/user/password/reset/done/'},name="password_reset"),
    url(r'^user/password/reset/done/$',password_reset_done,name="password_reset_done"),
    url(r'^user/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, {'post_reset_redirect' : '/login'},name="password_reset_confirm"),
    # url(r'^user/password/done/$', password_reset_complete),

    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]
handler404 = 'pages.views.page_not_found'
handler500  = 'pages.views.page_not_found'
