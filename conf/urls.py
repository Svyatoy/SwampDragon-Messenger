"""conf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import django.contrib.auth.views
import confs.views
import login
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
# from django.contrib.gis import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from login.views import *

urlpatterns = [
    url(r'^$', confs.views.home, name='home'),
    url(r'^home/$', confs.views.home),
    url(r'^admin/', admin.site.urls),
    url(r'^conferences/', include('confs.urls')),
    url(r'^news/', include('news.urls')),
    url(r'^companies/', include('companies.urls')),
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^login/$', django.contrib.auth.views.login),
    url(r'^account/', include('login.urls')),
    url(r'^logout/$', logout_page),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
