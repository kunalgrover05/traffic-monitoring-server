from django.conf.urls import url, include
from .models import BTData
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class BTDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BTData
        fields = ('bt_id', 'hardware_id')

# ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'/', BTDataSerializer)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]
