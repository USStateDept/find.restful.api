from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    CategoryListAPIView,
    CategoryDetailByIdAPIView,
    CategoryDetailAPIView,
    )

urlpatterns = [
    url(r'^$', CategoryDetailAPIView.as_view(), name='categories_details'),
    url(r'^list/$', CategoryListAPIView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', CategoryDetailByIdAPIView.as_view(), name='id'),
]

urlpatterns = format_suffix_patterns(urlpatterns)