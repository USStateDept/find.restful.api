from categories.models import Category
from categories.serializers import CategoryListSerializer, CategoryDetailSerializer

from rest_framework.generics import ListAPIView, RetrieveAPIView

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
    # query = request.GET.get("q")
    # if query:
    return queryset_list

    