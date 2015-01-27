from django.shortcuts import render
from rest_framework import viewsets
from scaler.serializers import CompoundsSerializer, CompoundsFoodsSerializer
from scaler.models import Compounds, CompoundsFoods

class CompoundsViewSet(viewsets.ModelViewSet):
	queryset = Compounds.objects.all()
	serializer_class=CompoundsSerializer

class CompoundsFoodsViewSet(viewsets.ModelViewSet):
	queryset = CompoundsFoods.objects.all()
	serializer_class=CompoundsFoodsSerializer


# Create your views here.
