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

from apps.people.models import Person


rows = []

person_ids = list(
    Person.objects.values_list(
        "id",
        flat=True
    )
)

for person_id in person_ids:

    identity_types = [1, 2]

    if random.random() > 0.7:
        identity_types.append(3)

    for identity_type in identity_types:

        if identity_type == 1:

            identity_number = str(
                random.randint(
                    100000000000,
                    999999999999
                )
            )

        elif identity_type == 2:

            letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

            identity_number = (
                "".join(
                    random.choice(letters)
                    for _ in range(5)
                )
                + str(
                    random.randint(
                        1000,
                        9999
                    )
                )
                + random.choice(letters)
            )

        elif identity_type == 3:

            identity_number = (
                random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
                + str(
                    random.randint(
                        1000000,
                        9999999
                    )
                )
            )

        rows.append({
            "person_id": person_id,
            "identity_type": identity_type,
            "identity_number": identity_number,
            "is_verified": random.choice(
                [0, 1]
            ),
            "remarks": ""
        })

data = pd.DataFrame(rows)

data.to_csv(
    "person_identities.csv",
    index=False
)

print(
    f"Generated {len(data)} identities"
)