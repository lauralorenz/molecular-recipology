from rest_framework import serializers
from models import Compounds, CompoundsFoods, Foods

class FoodsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Foods
		fields = ['id', 'name']

class CompoundsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Compounds
		fields = ['id', 'moldb_average_mass']

class CompoundsFoodsSerializer(serializers.ModelSerializer):
	food_id = FoodsSerializer()
	compound_id = CompoundsSerializer()
	class Meta:
		model = CompoundsFoods
		depth = 2
		fields = ['id', 'compound_id', 'food_id']
