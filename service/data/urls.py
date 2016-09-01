from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    CountryDataAPIView,
    )

urlpatterns = [
    # NOTE: Took out the full list of data -> response is too long and we will never allow this request.
    url(r'^$', CountryDataAPIView.as_view(), name='country_data'),
    # url(r'^list/$', DataListAPIView.as_view(), name='list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)