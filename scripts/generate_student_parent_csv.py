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

from apps.students.models import Student
from apps.people.models import Person

rows = []

student_ids = list(
    Student.objects.values_list(
        "id",
        flat=True
    )
)

person_ids = list(
    Person.objects.values_list(
        "id",
        flat=True
    )
)

for student_id in student_ids:

    father_id = random.choice(
        person_ids
    )

    mother_id = random.choice(
        person_ids
    )

    while mother_id == father_id:

        mother_id = random.choice(
            person_ids
        )

    rows.append({

        "student_id": student_id,

        "person_id": father_id,

        "relationship_type": 1,

        "is_primary_contact": 1,

        "can_pickup_student": 1,

        "receives_sms": 1,

        "receives_whatsapp": 1,

        "receives_email": 1,

        "remarks": ""
    })

    rows.append({

        "student_id": student_id,

        "person_id": mother_id,

        "relationship_type": 2,

        "is_primary_contact": 0,

        "can_pickup_student": 1,

        "receives_sms": 1,

        "receives_whatsapp": 1,

        "receives_email": 1,

        "remarks": ""
    })

data = pd.DataFrame(rows)

data.to_csv(
    "student_parents.csv",
    index=False
)

print(
    f"{len(data)} relationships generated"
)