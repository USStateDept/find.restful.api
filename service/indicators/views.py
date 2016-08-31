from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Indicator
from .serializers import IndicatorListSerializer


class IndicatorListAPIView(ListAPIView):
  """
  Retrieve a list of all indicators.
  """
  queryset = Indicator.objects.all()
  serializer_class = IndicatorListSerializer

class IndicatorDetailAPIView(ListAPIView):
  """
  Retrive a subcountry by name.
  """
  serializer_class = IndicatorListSerializer

  def get_queryset(self, *args, **kwargs):
    queryset_list = Indicator.objects.all()
    indicator_name = self.kwargs['indicator_name']
    print(indicator_name)
    if indicator_name is not None:
      queryset_list = queryset_list.filter(indicator_name=indicator_name)
    return queryset_list