from rest_framework import serializers

from .models import Region

class RegionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = [
            'region_id',
            'name',
            'type'
        ]