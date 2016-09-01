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
  Retrive a country's data for a specific indicator - default for all years.
  """
  # lookup_url_kwarg = 'indicator_id' FEATURE to lookup pending on the url key word
  serializer_class = DataListSerializer

  def get_queryset(self, *args, **kwargs):
    queryset_list = Data.objects.all()
    country_id = self.kwargs['country_id']
    indicator_id = self.kwargs['indicator_id']
    print(country_id)
    print(indicator_id)
    if country_id and indicator_id is not None:
      queryset_list = queryset_list.filter(country_id=country_id)
      queryset_list = queryset_list.filter(indicator_id=indicator_id)
    return queryset_list

class CountryDataYearAPIView(ListAPIView):
  """
  Retrive a country's data for a specific indicator - default for all years.
  """
  # lookup_url_kwarg = 'indicator_id' FEATURE to lookup pending on the url key word
  serializer_class = DataListSerializer

  def get_queryset(self, *args, **kwargs):
    queryset_list = Data.objects.all()
    country_id = self.kwargs['country_id']
    indicator_id = self.kwargs['indicator_id']
    year = self.kwargs['date']
    print(country_id)
    print(indicator_id)
    print(year)
    if country_id and indicator_id and year is not None:
      queryset_list = queryset_list.filter(country_id=country_id)
      queryset_list = queryset_list.filter(indicator_id=indicator_id)
      queryset_list = queryset_list.filter(date=year)
    return queryset_list