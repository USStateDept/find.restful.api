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
  Retrive a subcountry by name. \n
  /countries/?country=United States of America
  """
  serializer_class = CountryListSerializer

  def get_queryset(self, *args, **kwargs):
    query_params = self.request.query_params
    countries = query_params.get('country', None)
    # print('countries: ', countries)
    if countries is not None:
      queryset_list = Country.objects.all()
      queryset_list = queryset_list.filter(sub_country_name=countries)
      return queryset_list