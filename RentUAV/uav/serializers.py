from rest_framework import serializers 
from uav.models import Properties
 
 
class PropertySerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Properties
        fields = ('id',
                  'model',
                  'brand',
                  'weight',
                  'category')