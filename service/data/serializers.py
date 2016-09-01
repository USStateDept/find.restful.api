from rest_framework import serializers

from .models import Data

class DataListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = [
            'data_id',
            'date',
            'value',
            'createdat',
            'updatedat',
            'indicator_id',
            'country_id'
        ]