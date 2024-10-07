from django.core.management.base import BaseCommand
from farm_management.models import SensorData
from django.utils import timezone
from datetime import timedelta


class Command(BaseCommand):
    help = 'Clears sensor data older than 30 days'

    def handle(self, *args, **options):
        # Define the cutoff time (30 days ago)
        cutoff_time = timezone.now() - timedelta(days=30)

        # Delete old sensor data
        deleted_count, _ = SensorData.objects.filter(timestamp__lt=cutoff_time).delete()

        # Output the result
        self.stdout.write(f"Deleted {deleted_count} old sensor data records.")
