from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    CountryListAPIView,
    SubcountryDetailAPIView
    )

urlpatterns = [
    url(r'^$', CountryListAPIView.as_view(), name='list'),
    url(r'^(?P<sub_country_name>[\w, ]+)/subcountry/$', SubcountryDetailAPIView.as_view(), name='sub_country_name'),
]

urlpatterns = format_suffix_patterns(urlpatterns)