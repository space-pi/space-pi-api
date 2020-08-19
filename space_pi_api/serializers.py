from rest_framework import serializers 
from space_pi_api.models import TempHistory
from space_pi_api.models import HumidityHistory
 
 
class TempHistorySerializer(serializers.ModelSerializer):
 
    class Meta:
        model = TempHistory
        fields = ('id',
                  'reading',
                  'datetime',
                  'sensor')

class HumidityHistorySerializer(serializers.ModelSerializer):
 
    class Meta:
        model = HumidityHistory
        fields = ('id',
                  'reading',
                  'datetime',
                  'sensor')
