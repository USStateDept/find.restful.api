from slugify import slugify
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Category
from .serializers import CategoryListSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

class CategoryListAPIView(ListAPIView):
  """
  Retrieve a list of all categories.
  """
  # check if logged in
  permission_classes = (IsAuthenticated,)
  authentication_classes = (JSONWebTokenAuthentication,)

  queryset = Category.objects.all()
  serializer_class = CategoryListSerializer

class CategoryDetailByIdAPIView(RetrieveAPIView):
  """
  Retrieve a category by id.
  """
  # check if logged in
  permission_classes = (IsAuthenticated,)
  authentication_classes = (JSONWebTokenAuthentication,)

  queryset = Category.objects.all()
  serializer_class = CategoryListSerializer

class CategoryDetailAPIView(ListAPIView):
  """
  Retrive a category and/or subcategory by name. \n
  Delimiter is | between values you want to query by. \n
  /categories/?category=Health|Economic Growth (OR) \n
  /categories/?subcategory=General (OR) \n
  /categories/?category=Health&subcategory=General
  """
  # check if logged in
  permission_classes = (IsAuthenticated,)
  authentication_classes = (JSONWebTokenAuthentication,)
  
  serializer_class = CategoryListSerializer

  def get_queryset(self, *args, **kwargs):
    query_params = self.request.query_params
    categories = query_params.get('category', None)
    subcategories = query_params.get('subcategory', None)
    
    # create empty lists for parameters to be filtered by
    categoryParams = []
    subcategoryParams = []
    
    # create the lists based on the query params
    if categories is not None:
      for category in categories.split('|'):
        # TODO: figure out slugifying to query by non-case sensitive values for Postgres
        # category = slugify(category, separator="+")
        category = category.replace("%20", " ")
        categoryParams.append(str(category))
    if subcategories is not None:
      for subcategory in subcategories.split('|'):
        # subcategory = slugify(subcategory, separator="+")
        subcategory = subcategory.replace("%20", " ")
        subcategoryParams.append(str(subcategory))
    
    # filter based on the parameters
    if categories and subcategories is not None:
      print(categoryParams)
      print(subcategoryParams)
      queryset_list = Category.objects.all()
      queryset_list = queryset_list.filter(category_name__in=categoryParams).filter(sub_category_name__in=subcategoryParams)
      return queryset_list
    if categories is not None:
      print(categoryParams)
      queryset_list = Category.objects.all()
      queryset_list = queryset_list.filter(category_name__in=categoryParams)
      return queryset_list
    if subcategories is not None:
      print(subcategoryParams)
      queryset_list = Category.objects.all()
      queryset_list = queryset_list.filter(sub_category_name__in=subcategoryParams)
      return queryset_list