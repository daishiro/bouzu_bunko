"""bouzu_bunko URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth_ctrl/login', 'django.contrib.auth.views.login', {'template_name': 'auth_ctrl/login.html'}),
    url(r'^auth_ctrl/logout', 'django.contrib.auth.views.logout', {'template_name': 'auth_ctrl/logout.html'}),
    url(r'^hondana/', include('hondana.urls', namespace='hondana')),
]
