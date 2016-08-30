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
    url(r'^(?P<category_name>[\w, ]+)/category/$', CategoryDetailAPIView.as_view(), name='category_detail'),
    url(r'^(?P<sub_category_name>[\w, ]+)/subcategory/$', SubcategoryDetailAPIView.as_view(), name='sub_category_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)