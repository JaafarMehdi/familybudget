from rest_framework import serializers

from ..models.entry import Entry

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ['creator', 'name', 'amount', 'categories', 'list']
