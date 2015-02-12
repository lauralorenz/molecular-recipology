from rest_framework import serializers
from models import Compounds, Foods
import re


class FoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foods
        fields = ['id', 'name']


class CompoundsSerializer(serializers.ModelSerializer):
    density = serializers.SerializerMethodField('prepare_density')
    class Meta:
        model = Compounds
        fields = ['id', 'moldb_average_mass', 'density']

    def prepare_density(self, obj):
        return re.search('(?<= )(?:\d\.)?\d+', obj.density).group(0)


class CompoundsFoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foods
        fields = ['id', 'name', 'compounds']

