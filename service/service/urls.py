"""service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
# from django.contrib.auth.models import User, Group
from django.contrib import admin
# admin.autodiscover()

# from rest_framework import permissions, routers, serializers, viewsets

# from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope


# first we define the serializers
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User


# class GroupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Group


# ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class GroupViewSet(viewsets.ModelViewSet):
#     permission_classes = [permissions.IsAuthenticated, TokenHasScope]
#     required_scopes = ['groups']
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer


# Routers provide an easy way of automatically determining the URL conf
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'groups', GroupViewSet)


urlpatterns = [
    # url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', include('rest_framework_docs.urls')),
    # url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    # API
    url(r'^categories/', view=include('categories.urls', namespace='categories')),
    url(r'^countries/', view=include('countries.urls', namespace='countries')),
    url(r'^countries/data/', view=include('data.urls', namespace='country_data')),
    url(r'^indicators/', view=include('indicators.urls', namespace='indicators')),
    url(r'^regions/', view=include('regions.urls', namespace='regions')),
    url(r'^regions/data/', view=include('region_data.urls', namespace='region_data')),
]
