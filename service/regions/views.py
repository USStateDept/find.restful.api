from rest_framework.generics import ListAPIView

from .models import Region
from .serializers import RegionListSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class RegionListAPIView(ListAPIView):
  """
  Retrieve a list of all indicators.
  """
  # check if logged in
  permission_classes = (IsAuthenticated,)
  authentication_classes = (TokenAuthentication,)

  queryset = Region.objects.all()
  serializer_class = RegionListSerializer

class RegionDetailAPIView(ListAPIView):
  """
  Retrive a region by id(s). \n
  Delimiter is | between all the values in your parameters for each variable. \n
  /regions/?region=4|5|6
  """
  # check if logged in
  permission_classes = (IsAuthenticated,)
  authentication_classes = (TokenAuthentication,)

  serializer_class = RegionListSerializer

  def get_queryset(self, *args, **kwargs):
    query_params = self.request.query_params
    regions = query_params.get('region', None)

    # create an empty list for parameters to be filters by 
    regionParams = []

    # create the list based on the query parameters
    if regions is not None:
      for region in regions.split('|'):
        region = region.replace("%20", " ")
        regionParams.append(int(region))

    # print('region id: ', regions)

    # filter by the parameters
    if regions is not None:
      queryset_list = Region.objects.all()
      queryset_list = queryset_list.filter(region_id__in=regionParams)
      return queryset_list