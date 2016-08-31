from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Data
from .serializers import DataListSerializer


class DataListAPIView(ListAPIView):
  """
  Retrieve a list of all indicators.
  """
  queryset = Data.objects.all()
  serializer_class = DataListSerializer

# class IndicatorDetailAPIView(ListAPIView):
#   """
#   Retrive a subcountry by name.
#   """
#   serializer_class = DataListSerializer

#   def get_queryset(self, *args, **kwargs):
#     queryset_list = Data.objects.all()
#     indicator_name = self.kwargs['indicator_name']
#     print(indicator_name)
#     if indicator_name is not None:
#       queryset_list = queryset_list.filter(indicator_name=indicator_name)
#     return queryset_list
