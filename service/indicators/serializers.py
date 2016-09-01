from rest_framework import serializers

from .models import Indicator

class IndicatorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicator
        fields = [
            # Don't want to show some of these details.'
            'indicator_id',
            'indicator_name',
            'indicator_url',
            'indicator_data_url',
            'direct_indicator_source',
            'original_indicator_source',
            'update_cycle',
            'scope',
            'units',
            'last_source_update_ts',
            'when_to_update_ts',
            'indicator_definition',
            # 'createdat',
            # 'updatedat',
            'avg_equal',
            'avg_population',
            'avg_gdp'
        ]