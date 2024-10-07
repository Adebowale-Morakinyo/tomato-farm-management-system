from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FarmViewSet, CropViewSet, SensorViewSet, SensorDataViewSet

router = DefaultRouter()
router.register(r'farms', FarmViewSet)
router.register(r'crops', CropViewSet)
router.register(r'sensors', SensorViewSet)
router.register(r'sensor-data', SensorDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
