from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Category
from .serializers import CategoryListSerializer, CategoryDetailSerializer

class CategoryListAPIView(ListAPIView):
  """
  Retrieve a list of all categories.
  """
  queryset = Category.objects.all()
  serializer_class = CategoryListSerializer

class CategoryDetailByIdAPIView(RetrieveAPIView):
  """
  Retrieve a category by id.
  """
  queryset = Category.objects.all()
  serializer_class = CategoryListSerializer

class CategoryDetailAPIView(ListAPIView):
  """
  Retrive a category by name.
  """
  # lookup_url_kwarg = 'category_name' FEATURE to lookup pending on the url key word
  serializer_class = CategoryListSerializer

  def get_queryset(self, *args, **kwargs):
    queryset_list = Category.objects.all()
    category_name = self.kwargs['category_name']
    print(category_name)
    if category_name is not None:
      queryset_list = queryset_list.filter(category_name=category_name)
    return queryset_list

class SubcategoryDetailAPIView(ListAPIView):
  """
  Retrive a subcategory by name.
  """
  serializer_class = CategoryListSerializer

  def get_queryset(self, *args, **kwargs):
    queryset_list = Category.objects.all()
    sub_category_name = self.kwargs['sub_category_name']
    print(sub_category_name)
    if sub_category_name is not None:
      queryset_list = queryset_list.filter(sub_category_name=sub_category_name)
    return queryset_list
    