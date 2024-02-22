from rest_framework import viewsets
from . import models
from . import serializers

class RentedUavsViewset(viewsets.ModelViewSet):
    queryset = models.RentedUavs.objects.all()
    serializer_class = serializers.PropertySerializer

# list(), retrieve(), create(), update(), destroy()