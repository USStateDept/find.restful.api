from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Category
from .serializers import CategoryListSerializer

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
  Retrive a category and/or subcategory by name. \n
  /categories/?category=Health (OR) \n
  /categories/?subcategory=General (OR) \n
  /categories/?category=Health&subcategory=General
  """
  serializer_class = CategoryListSerializer

  def get_queryset(self, *args, **kwargs):
    query_params = self.request.query_params
    categories = query_params.get('category', None)
    subcategories = query_params.get('subcategory', None)
    
    # print('categories: ', categories)
    # print('subcategories: ',subcategories)
    if categories and subcategories is not None:
      queryset_list = Category.objects.all()
      queryset_list = queryset_list.filter(category_name=categories)
      queryset_list = queryset_list.filter(sub_category_name=subcategories)
      return queryset_list
    if categories is not None:
      queryset_list = Category.objects.all()
      queryset_list = queryset_list.filter(category_name=categories)
      return queryset_list
    if subcategories is not None:
      queryset_list = Category.objects.all()
      queryset_list = queryset_list.filter(sub_category_name=subcategories)
      return queryset_list