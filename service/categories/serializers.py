from rest_framework import serializers

from .models import Category

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'category_id',
            'category_name',
            'sub_category_name',
            'createdat',
            'updatedat'
        ]


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'category_name',
            'sub_category_name'
        ]