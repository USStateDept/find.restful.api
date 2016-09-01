from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Data
from .serializers import DataListSerializer

# NOTE: Took out the full list of data -> response is too long and we will never allow this request.
# class DataListAPIView(ListAPIView):
#   """
#   Retrieve a list of all indicators.
#   """
#   queryset = Data.objects.all()
#   serializer_class = DataListSerializer

class CountryDataAPIView(ListAPIView):
  """
  Retrive a country's data for a specific indicator - default for all years. \n
  /data/?country=202&indicator=22 (OR) \n
  /data/?country=202&indicator=22&year=2015 \n
  """
  serializer_class = DataListSerializer

  def get_queryset(self, *args, **kwargs):
    query_params = self.request.query_params
    countries = query_params.get('country', None)
    indicators = query_params.get('indicator', None)
    year = query_params.get('year', None)
    # print('countries: ', countries)
    # print('indicators: ', indicators)
    # print('year: ', year)
    if countries and indicators and year is not None:
      queryset_list = Data.objects.all()
      queryset_list = queryset_list.filter(country_id=countries)
      queryset_list = queryset_list.filter(indicator_id=indicators)
      queryset_list = queryset_list.filter(date=year)
      return queryset_list
    if countries and indicators is not None and year is None:
      queryset_list = Data.objects.all()
      queryset_list = queryset_list.filter(country_id=countries)
      queryset_list = queryset_list.filter(indicator_id=indicators)
      return queryset_list