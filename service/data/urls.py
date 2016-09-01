from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    CountryDataAPIView,
    CountryDataYearAPIView
    )

urlpatterns = [
    # NOTE: Took out the full list of data -> response is too long and we will never allow this request.
    # url(r'^$', DataListAPIView.as_view(), name='list'),
    url(r'^(?P<country_id>\d+)/country/(?P<indicator_id>\d+)/indicator/$', CountryDataAPIView.as_view(), name='country_data'),
    url(r'^(?P<country_id>\d+)/country/(?P<indicator_id>\d+)/indicator/(?P<date>\d{4})/year/$', CountryDataYearAPIView.as_view(), name='country_data_year'),
]

urlpatterns = format_suffix_patterns(urlpatterns)