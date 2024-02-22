from rest_framework import serializers 
from uav.models import RentedUavs
 
 
class RentedSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = RentedUavs
        fields = ('id',
                  'uav',
                  'date',
                  'member',)