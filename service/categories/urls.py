from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    CategoryListAPIView,
    CategoryDetailByIdAPIView,
    CategoryDetailAPIView
    )

urlpatterns = [
    url(r'^$', CategoryListAPIView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', CategoryDetailByIdAPIView.as_view(), name='id'),
    url(r'^(?P<category_name>[\w-]+)/$', CategoryDetailAPIView.as_view(), name='detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)