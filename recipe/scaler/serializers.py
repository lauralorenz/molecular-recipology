from rest_framework import serializers
from models import Compounds, Foods


class FoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foods
        fields = ['id', 'name']


class CompoundsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compounds
        fields = ['id', 'moldb_average_mass', 'density']


class CompoundsFoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foods
        fields = ['id', 'name', 'compounds']

