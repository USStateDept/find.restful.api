from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    CategoryListAPIView,
    CategoryDetailByIdAPIView,
    CategoryDetailAPIView,
    SubcategoryDetailAPIView
    )

urlpatterns = [
    url(r'^$', CategoryListAPIView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', CategoryDetailByIdAPIView.as_view(), name='id'),
    url(r'^category/(?P<category_name>[\w, ]+)/$', CategoryDetailAPIView.as_view(), name='category_detail'),
    url(r'^subcategory/(?P<sub_category_name>[\w, ]+)/$', SubcategoryDetailAPIView.as_view(), name='sub_category_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)