from rest_framework import routers, serializers
from .models import TrafficData

# Serializers define the API representation.
class TrafficDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TrafficData
