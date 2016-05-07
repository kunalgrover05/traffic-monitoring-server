from rest_framework import viewsets
from .models import TrafficData
from .serializers import TrafficDataSerializer

class TrafficDataViewSet(viewsets.ModelViewSet):
    queryset = TrafficData.objects.all()
    serializer_class = TrafficDataSerializer