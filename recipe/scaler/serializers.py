from rest_framework import serializers
from models import Compounds, CompoundsFoods, Foods

class FoodsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Foods
		fields = ['id', 'name']

class CompoundsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Compounds
		fields = ['id', 'moldb_average_mass', 'density']

class CompoundsFoodsSerializer(serializers.ModelSerializer):
	food_id = FoodsSerializer()
	compound_id = CompoundsSerializer()
	class Meta:
		model = CompoundsFoods
		fields = ['id','compound_id', 'food_id']
