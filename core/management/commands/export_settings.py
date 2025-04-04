from django.core.management.base import BaseCommand
from django.conf import settings
import json
import os

class Command(BaseCommand):
    help = "Export all Django settings to a JSON file"

    def handle(self, *args, **kwargs):
        settings_dict = {key: getattr(settings, key) for key in dir(settings) if key.isupper()}
        env = os.getenv('DJANGO_ENV', 'default')
        filename = f"settings_{env}.json"

        with open(filename, "w") as f:
            json.dump(settings_dict, f, indent=4, default=str)

        self.stdout.write(self.style.SUCCESS(f"Settings exported to {filename}"))
