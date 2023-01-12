from rest_framework import serializers
from .models import Beer


class BeerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beer
        fields = ['id', 'name', 'brand', 'cost_per_liter', 'flow_volume', 'type', 'times_used']
