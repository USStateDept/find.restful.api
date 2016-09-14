from rest_framework import serializers

from .models import Country

class CountryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = [
            'country_id',
            'country_name',
            'name',
            'dod_group',
            'dos_group',
            'usaid_group',
            'income_group',
            'iso'
        ]