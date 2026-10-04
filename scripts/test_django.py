import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(BASE_DIR))

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "campusiq.settings"
)

import django

django.setup()

from apps.people.models import Person

print(
    "Persons:",
    Person.objects.count()
)