from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    IndicatorListAPIView,
    IndicatorDetailAPIView
    )

urlpatterns = [
    url(r'^$', IndicatorDetailAPIView.as_view(), name='indicator_name'),
    url(r'^list/$', IndicatorListAPIView.as_view(), name='list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)