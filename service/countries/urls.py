from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    CountryListAPIView,
    CountryDetailAPIView
    )

urlpatterns = [
    url(r'^$', CountryDetailAPIView.as_view(), name='country_name'),
    url(r'^list/$', CountryListAPIView.as_view(), name='list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)