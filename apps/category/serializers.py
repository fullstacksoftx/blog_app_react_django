from .models import *
from rest_framework import serializers


class CategorySerializer(serializers.Serializer):
    thumbnail = serializers.CharField(source='get_thumbnail')

    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'thumbnail',
        ]
