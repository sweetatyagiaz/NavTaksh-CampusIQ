import os
import sys
import random
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(BASE_DIR))

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "campusiq.settings"
)

import django

django.setup()

import pandas as pd

from faker import Faker

from apps.people.models import Person

fake = Faker("en_IN")

rows = []

person_ids = list(
    Person.objects.values_list(
        "id",
        flat=True
    )
)

for person_id in person_ids:

    contacts = [
        {
            "contact_type": 1,  # Mobile
            "value": fake.msisdn()[:10],
            "is_primary": True,
            "is_verified": True
        },
        {
            "contact_type": 2,  # Email
            "value": fake.email(),
            "is_primary": False,
            "is_verified": random.choice([0, 1])
        }
    ]

    if random.random() > 0.30:

        contacts.append({
            "contact_type": 3,  # WhatsApp
            "value": fake.msisdn()[:10],
            "is_primary": False,
            "is_verified": random.choice([0, 1])
        })

    if random.random() > 0.50:

        contacts.append({
            "contact_type": 4,  # Alternate Mobile
            "value": fake.msisdn()[:10],
            "is_primary": False,
            "is_verified": False
        })

    for contact in contacts:

        rows.append({
            "person_id": person_id,
            "contact_type": contact["contact_type"],
            "value": contact["value"],
            "is_primary": contact["is_primary"],
            "is_verified": contact["is_verified"],
            "remarks": ""
        })

data = pd.DataFrame(rows)

data.to_csv(
    "person_contacts.csv",
    index=False
)

print(
    f"Generated {len(data)} contacts"
)