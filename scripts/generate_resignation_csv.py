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

from apps.hr.models import Employment

rows = []

reason_types = [
    1,  # RESIGNED
    2,  # RETIRED
    3,  # TERMINATED
    4,  # CONTRACT_ENDED
    5,  # TRANSFERRED
    6,  # DECEASED
    7,  # ABSCONDED
    99  # OTHER
]

employments = Employment.objects.filter(
    is_current=False,
    relieving_date__isnull=False
)

for employment in employments:

    reason_type = random.choice(
        reason_types
    )

    rows.append({

        "slug": (
            f"res-"
            f"{employment.employee_code.lower()}"
        ),

        "employment_id": employment.id,

        "reason_type": reason_type,

        "resignation_date": (
            employment.relieving_date
        ),

        "reason_details": (
            f"Reason {reason_type}"
        ),

        "exit_interview_notes": (
            "Generated demo data"
        ),

        "is_rehire_eligible": random.choice(
            [True, False]
        )
    })

data = pd.DataFrame(rows)

data.to_csv(
    "resignations.csv",
    index=False
)

print(
    f"{len(data)} resignations generated"
)