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
  Retrive a indicator by name. \n
  /indicators/?indicator=Poverty gap at $1.90 a day (2011 PPP)
  """
  serializer_class = IndicatorListSerializer

  def get_queryset(self, *args, **kwargs):
    query_params = self.request.query_params
    indicators = query_params.get('indicator', None)
    # print('indicator name: ', indicators)
    if indicators is not None:
      queryset_list = Indicator.objects.all()
      queryset_list = queryset_list.filter(indicator_name=indicators)
      return queryset_list