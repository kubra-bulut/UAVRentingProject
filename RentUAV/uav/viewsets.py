from rest_framework import viewsets
from . import models
from . import serializers

class PropertiesViewset(viewsets.ModelViewSet):
    queryset = models.Properties.objects.all()
    serializer_class = serializers.PropertySerializer

# list(), retrieve(), create(), update(), destroy()