"""service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
# from rest_framework import routers

urlpatterns = [
    # url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', include('rest_framework_docs.urls')),

    # API
    url(r'^categories/', view=include('categories.urls', namespace='categories')),
    url(r'^countries/', view=include('countries.urls', namespace='countries')),
    url(r'^data/', view=include('data.urls', namespace='data')),
    url(r'^indicators/', view=include('indicators.urls', namespace='indicators')),
    url(r'^regions/', view=include('regions.urls', namespace='regions')),
]
