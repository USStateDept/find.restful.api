from rest_framework import serializers

from .models import RegionData

class RegionDataListSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegionData
        fields = [
            # Don't want to show some of these details.'
            'region_data',
            'indicator_id',
            'region_id',
            'year',
            'avg'
            # 'createdat',
            # 'updatedat'
        ]