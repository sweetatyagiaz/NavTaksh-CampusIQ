import os
import sys
import random
from pathlib import Path
from datetime import date, timedelta

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
from apps.organizations.models import School
from apps.hr.models import Department
from apps.hr.models import Designation

persons = list(
    Person.objects.values_list(
        "id",
        flat=True
    )
)

schools = list(
    School.objects.values_list(
        "id",
        flat=True
    )
)

departments = list(
    Department.objects.values_list(
        "id",
        flat=True
    )
)

designations = list(
    Designation.objects.values_list(
        "id",
        flat=True
    )
)

TOTAL = min(
    50000,
    len(persons)
)

rows = []

for index, person_id in enumerate(
    persons[:TOTAL],
    start=1
):

    joining_date = date(
        random.randint(2015, 2026),
        random.randint(1, 12),
        random.randint(1, 28)
    )

    # 20% employees left
    has_left = random.random() < 0.20

    relieving_date = None
    is_current = True

    if has_left:

        relieving_date = joining_date + timedelta(
            days=random.randint(
                180,
                2500
            )
        )

        if relieving_date > date.today():

            relieving_date = None

        else:

            is_current = False

    employee_code = (
        f"EMP{index:06d}"
    )

    rows.append({

        "slug": employee_code.lower(),

        "person_id": person_id,

        "school_id": random.choice(
            schools
        ),

        "department_id": random.choice(
            departments
        ),

        "designation_id": random.choice(
            designations
        ),

        "employee_code": employee_code,

        "joining_date": joining_date,

        "relieving_date": relieving_date,

        "is_current": is_current
    })

data = pd.DataFrame(rows)

data.to_csv(
    "employments.csv",
    index=False
)

print(
    f"{len(data)} employments generated"
)