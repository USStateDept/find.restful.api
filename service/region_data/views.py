from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework_tracking.mixins import LoggingMixin

from .models import RegionData
from .serializers import RegionDataListSerializer

# from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

class RegionDataAPIView(LoggingMixin, ListAPIView):
  """
  Retrive a region(s)' data for a specific indicator - default for all years. \n
  Delimiter is | between all the values in your parameters for each variable. \n
  /regions/data/?region=202&indicator=22 (OR) \n
  /regions/data/?region=202&indicator=22&year=2015 \n
  """
  # check if logged in
  # permission_classes = (IsAuthenticated,)
  authentication_classes = (JSONWebTokenAuthentication,)
  throttle_scope = 'generic'

  serializer_class = RegionDataListSerializer

  def get_queryset(self, *args, **kwargs):
    query_params = self.request.query_params
    regions = query_params.get('region', None)
    indicators = query_params.get('indicator', None)
    years = query_params.get('year', None)

    # create an empty list for parameters to be filters by 
    regionParams = []
    indicatorParams = []
    yearParams = []

    # print(regions)
    # print(indicators)

    # create the list based on the query parameters
    if regions is not None:
      for region in regions.split('|'):
        region = region.replace("%20", " ")
        regionParams.append(int(region))
    if indicators is not None:
      for indicator in indicators.split('|'):
        indicator = indicator.replace("%20", " ")
        indicatorParams.append(int(indicator))
    if years is not None:
      for year in years.split('|'):
        year = year.replace("%20", " ")
        yearParams.append(int(year))

    # print('regions: ', regionParams)
    # print('indicators: ', indicatorParams)
    # print('year: ', yearParams)

    # filter by the parameters
    if regions and indicators and years is not None:
      queryset_list = RegionData.objects.all()
      queryset_list = queryset_list.filter(region_id__in=regionParams)
      queryset_list = queryset_list.filter(indicator_id__in=indicatorParams)
      queryset_list = queryset_list.filter(year__in=yearParams)
      return queryset_list
    if regions and indicators is not None and years is None:
      queryset_list = RegionData.objects.all()
      queryset_list = queryset_list.filter(region_id__in=regionParams)
      queryset_list = queryset_list.filter(indicator_id__in=indicatorParams)
      return queryset_list
    # return 404