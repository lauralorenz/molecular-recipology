from django.shortcuts import render
from rest_framework import viewsets
from serializers import CompoundsSerializer, CompoundsFoodsSerializer, FoodsSerializer
from models import Compounds, CompoundsFoods, Foods

class CompoundsViewSet(viewsets.ModelViewSet):
    queryset = Compounds.objects.all()
    serializer_class = CompoundsSerializer
    filter_fields=('id','moldb_average_mass','density')

class FoodsViewSet(viewsets.ModelViewSet):
    queryset = Foods.objects.all()
    serializer_class = FoodsSerializer
    filter_fields=('id','name')

class CompoundsFoodsViewSet(viewsets.ModelViewSet):
    queryset = CompoundsFoods.objects.all()
    serializer_class = CompoundsFoodsSerializer


def index(request):
    return render(request, 'index.html', {})


# Create your views here.
