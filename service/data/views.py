from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Data
from .serializers import DataListSerializer

# from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

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
  Delimiter is | between all the values in your parameters for each variable. \n
  /countries/data/?country=202&indicator=22 (OR) \n
  /countries/data/?country=202&indicator=22&year=2015 \n
  """
  # check if logged in
  # permission_classes = (IsAuthenticated,)
  authentication_classes = (JSONWebTokenAuthentication,)

  serializer_class = DataListSerializer

  def get_queryset(self, *args, **kwargs):
    query_params = self.request.query_params
    countries = query_params.get('country', None)
    indicators = query_params.get('indicator', None)
    years = query_params.get('year', None)

    # create an empty list for parameters to be filters by 
    countryParams = []
    indicatorParams = []
    yearParams = []

    # create the list based on the query parameters
    if countries is not None:
      for country in countries.split('|'):
        country = country.replace("%20", " ")
        countryParams.append(int(country))
    if indicators is not None:
      for indicator in indicators.split('|'):
        indicator = indicator.replace("%20", " ")
        indicatorParams.append(int(indicator))
    if years is not None:
      for year in years.split('|'):
        year = year.replace("%20", " ")
        yearParams.append(int(year))

    # print('countries: ', countryParams)
    # print('indicators: ', indicatorParams)
    # print('year: ', yearParams)

    # filter by the parameters
    if countries and indicators and years is not None:
      queryset_list = Data.objects.all()
      queryset_list = queryset_list.filter(country_id__in=countryParams)
      queryset_list = queryset_list.filter(indicator_id__in=indicatorParams)
      queryset_list = queryset_list.filter(date__in=yearParams)
      return queryset_list
    if countries and indicators is not None and years is None:
      queryset_list = Data.objects.all()
      queryset_list = queryset_list.filter(country_id__in=countryParams)
      queryset_list = queryset_list.filter(indicator_id__in=indicatorParams)
      return queryset_list
    # return 404