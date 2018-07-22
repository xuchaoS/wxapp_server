from django.shortcuts import render
from rest_framework import serializers, viewsets
from rest_framework.permissions import AllowAny
from .models import Exchange


# Create your views here.

# Serializers define the API representation.
class ExchangeSerializer(serializers.HyperlinkedModelSerializer):
    time = serializers.DateTimeField('%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = Exchange
        fields = ('vef', 'cny', 'time', 'author')


# ViewSets define the view behavior.
class ExchangeViewSet(viewsets.ModelViewSet):
    queryset = Exchange.objects.all().order_by('-time')
    serializer_class = ExchangeSerializer
    permission_classes = (AllowAny,)
