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

from django.db.models import Q

from apps.hr.models import (
    Employment,
    Designation
)

from apps.academics.models import Subject

teacher_designation_ids = list(

    Designation.objects.filter(

        Q(name__startswith="PGT") |
        Q(name__startswith="TGT") |
        Q(name__startswith="PRT") |
        Q(name__icontains="Teacher")

    ).values_list(
        "id",
        flat=True
    )
)

teacher_employments = Employment.objects.filter(
    designation_id__in=teacher_designation_ids
)

subject_ids = list(
    Subject.objects.values_list(
        "id",
        flat=True
    )
)

print(
    f"Teachers: {teacher_employments.count()}"
)

print(
    f"Subjects: {len(subject_ids)}"
)

rows = []

for employment in teacher_employments:

    total_subjects = random.randint(
        1,
        3
    )

    selected_subjects = random.sample(
        subject_ids,
        min(
            total_subjects,
            len(subject_ids)
        )
    )

    for index, subject_id in enumerate(
        selected_subjects
    ):

        rows.append({

            "slug": (
                f"ts-"
                f"{employment.id}-"
                f"{subject_id}"
            ),

            "employment_id":
                employment.id,

            "subject_id":
                subject_id,

            "is_primary":
                index == 0,

            "remarks":
                ""
        })

data = pd.DataFrame(rows)

data.to_csv(
    "teacher_subjects.csv",
    index=False
)

print(
    f"{len(data)} teacher subject records generated"
)