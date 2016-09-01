from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Country
from .serializers import CountryListSerializer


class CountryListAPIView(ListAPIView):
  """
  Retrieve a list of all countries.
  """
  queryset = Country.objects.all()
  serializer_class = CountryListSerializer

class SubcountryDetailAPIView(ListAPIView):
  """
  Retrive a subcountry by name(s). \n
  Delimiter is | between country names. \n
  /countries/?country=United States of America
  """
  serializer_class = CountryListSerializer

  def get_queryset(self, *args, **kwargs):
    query_params = self.request.query_params
    countries = query_params.get('country', None)

    # create an empty list for parameters to be filters by 
    countryParams = []

    # create the list based on the query parameters
    if countries is not None:
      for country in countries.split('|'):
        countryParams.append(str(country))

    # print('countries: ', countries)
    if countries is not None:
      queryset_list = Country.objects.all()
      queryset_list = queryset_list.filter(sub_country_name__in=countryParams)
      return queryset_list