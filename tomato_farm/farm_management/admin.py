from django.contrib import admin
from .models import Farm, Crop, Sensor, SensorData


@admin.register(Farm)
class FarmAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'created_at')
    search_fields = ('name', 'location')


@admin.register(Crop)
class CropAdmin(admin.ModelAdmin):
    list_display = ('farm', 'crop_type', 'planted_at', 'harvest_estimate')
    list_filter = ('farm', 'crop_type')


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ('farm', 'name', 'sensor_type')
    list_filter = ('sensor_type', 'farm')


@admin.register(SensorData)
class SensorDataAdmin(admin.ModelAdmin):
    list_display = ('sensor', 'timestamp', 'value')
    list_filter = ('sensor', 'timestamp')
