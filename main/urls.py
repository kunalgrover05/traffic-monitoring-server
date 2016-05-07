from django.conf.urls import url, include
from rest_framework import routers
from .views import TrafficDataViewSet

router = routers.DefaultRouter()
router.register(r'api', TrafficDataViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]
