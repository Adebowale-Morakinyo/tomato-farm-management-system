from django.shortcuts import render
from rest_framework.response import Response
from django.core.cache import cache
from rest_framework import viewsets
from .models import Farm, Crop, Sensor, SensorData
from .serializers import FarmSerializer, CropSerializer, SensorSerializer, SensorDataSerializer


class FarmViewSet(viewsets.ModelViewSet):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer


class CropViewSet(viewsets.ModelViewSet):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorDataViewSet(viewsets.ModelViewSet):
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer

    def list(self, request, *args, **kwargs):
        # Check if the cache has the sensor data
        cached_data = cache.get('sensor_data')

        if cached_data is not None:
            return Response(cached_data)  # Return cached data

        # Otherwise, get the data from the database
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        response_data = serializer.data

        # Cache the data for 5 minutes
        cache.set('sensor_data', response_data, timeout=300)

        return Response(response_data)
