from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    RegionListAPIView,
    RegionDetailAPIView
    )

urlpatterns = [
    url(r'^$', RegionDetailAPIView.as_view(), name='region'),
    url(r'^list/$', RegionListAPIView.as_view(), name='list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)