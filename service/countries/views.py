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
  Retrive a subcountry by name.
  """
  serializer_class = CountryListSerializer

  def get_queryset(self, *args, **kwargs):
    queryset_list = Country.objects.all()
    sub_country_name = self.kwargs['sub_country_name']
    print(sub_country_name)
    if sub_country_name is not None:
      queryset_list = queryset_list.filter(sub_country_name=sub_country_name)
    return queryset_list