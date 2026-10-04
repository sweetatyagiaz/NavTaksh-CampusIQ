import os
import sys
import random
from pathlib import Path
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(BASE_DIR))

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "campusiq.settings"
)

import django

django.setup()

import pandas as pd

from apps.organizations.models import (
    SchoolBoardRegistration
)

rows = []

reason_types = [

    "VOLUNTARY",

    "BOARD_CHANGE",

    "NON_COMPLIANCE",

    "MERGER",

    "CLOSURE",

    "OTHER"
]

registrations = (
    SchoolBoardRegistration.objects.all()
)

for registration in registrations:

    # roughly 15% withdrawn

    if random.random() > 0.15:

        continue

    withdrawal_date = (
        registration.registration_date
        + timedelta(
            days=random.randint(
                365,
                3650
            )
        )
    )

    reason_type = random.choice(
        reason_types
    )

    rows.append({

        "registration_id":
            registration.id,

        "withdrawal_date":
            withdrawal_date,

        "reason_type":
            reason_type,

        "reason":
            f"{reason_type} generated data",

        "remarks":
            "Generated demo data"
    })

data = pd.DataFrame(rows)

data.to_csv(
    "school_board_withdrawals.csv",
    index=False
)

print(
    f"{len(data)} withdrawals generated"
)