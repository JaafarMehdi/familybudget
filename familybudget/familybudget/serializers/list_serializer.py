from rest_framework import serializers

from ..models.list import List

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        # todo make creator autoset
        fields = ['creator', 'name', 'sharers']
