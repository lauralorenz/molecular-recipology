from django.shortcuts import render
from rest_framework import viewsets
from serializers import CompoundsSerializer, CompoundsFoodsSerializer
from models import Compounds, CompoundsFoods
from django.views.generic import View

class CompoundsViewSet(viewsets.ModelViewSet):
	queryset = Compounds.objects.all()
	serializer_class=CompoundsSerializer

class CompoundsFoodsViewSet(viewsets.ModelViewSet):
	queryset = CompoundsFoods.objects.all()
	serializer_class=CompoundsFoodsSerializer


def intro(request):
    return render(request, 'intro.html', {})


# Create your views here.
