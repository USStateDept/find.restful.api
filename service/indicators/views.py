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
  Delimiter is | between all the values in your parameters for each variable. \n
  /indicators/?indicator=Poverty gap at $1.90 a day (2011 PPP)|Physical Integrity Index
  """
  serializer_class = IndicatorListSerializer

  def get_queryset(self, *args, **kwargs):
    query_params = self.request.query_params
    indicators = query_params.get('indicator', None)

    # create an empty list for parameters to be filters by 
    indicatorParams = []

    # create the list based on the query parameters
    if indicators is not None:
      for indicator in indicators.split('|'):
        indicator = indicator.replace("%20", " ")
        indicatorParams.append(str(indicator))

    # print('indicator name: ', indicators)

    # filter by the parameters
    if indicators is not None:
      queryset_list = Indicator.objects.all()
      queryset_list = queryset_list.filter(indicator_name__in=indicatorParams)
      return queryset_list