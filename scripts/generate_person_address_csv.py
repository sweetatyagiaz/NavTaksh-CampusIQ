import random, sys
import os
import django
import pandas as pd
from pathlib import Path

from faker import Faker

BASE_DIR = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(BASE_DIR))

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "campusiq.settings"
)

import django

django.setup()

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

    address_count = random.choice([1, 1, 1, 2])

    used_types = set()

    for index in range(address_count):

        address_type = random.choice(
            [1, 2, 3]
        )

        while address_type in used_types:
            address_type = random.choice(
                [1, 2, 3]
            )

        used_types.add(address_type)

        rows.append({
            "person_id": person_id,
            "address_type": address_type,
            "address_line_1": fake.street_address(),
            "address_line_2": random.choice([
                "",
                f"Near {fake.company()}",
                f"Sector {random.randint(1, 99)}",
                f"Block {random.choice(['A','B','C','D'])}"
                ]),
            "landmark": fake.company(),
            "city": fake.city(),
            "district": fake.city(),
            "state": fake.state(),
            "country": "India",
            "postal_code": fake.postcode(),
            "latitude": round(
                random.uniform(
                    8.0,
                    37.0
                ),
                7
            ),
            "longitude": round(
                random.uniform(
                    68.0,
                    97.0
                ),
                7
            ),
            "is_primary": index == 0,
            "remarks": ""
        })

data = pd.DataFrame(rows)

data.to_csv(
    "person_addresses.csv",
    index=False
)

print(
    f"Generated {len(data)} addresses"
)