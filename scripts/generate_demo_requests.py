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

from faker import Faker

from apps.contact.models import DemoRequest

fake = Faker("en_IN")

TOTAL_RECORDS = 100


def create_demo_requests():

    DemoRequest.objects.all().delete()

    institution_types = [
        DemoRequest.InstitutionType.SCHOOL,
        DemoRequest.InstitutionType.COLLEGE,
        DemoRequest.InstitutionType.UNIVERSITY,
        DemoRequest.InstitutionType.COACHING,
        DemoRequest.InstitutionType.TRAINING,
    ]

    status_weights = [
        DemoRequest.Status.NEW,
        DemoRequest.Status.NEW,
        DemoRequest.Status.NEW,
        DemoRequest.Status.CONTACTED,
        DemoRequest.Status.CONTACTED,
        DemoRequest.Status.QUALIFIED,
        DemoRequest.Status.DEMO_SCHEDULED,
        DemoRequest.Status.CONVERTED,
        DemoRequest.Status.REJECTED,
    ]

    institutions = [
        "Delhi Public School",
        "Modern School",
        "Ryan International School",
        "DAV Public School",
        "St. Xavier's School",
        "ABC Engineering College",
        "National Institute of Technology",
        "Future Skills Academy",
        "Bright Future Coaching",
        "Tech Learning Center",
    ]

    data = []

    for _ in range(TOTAL_RECORDS):

        institution_type = random.choice(
            institution_types
        )

        status = random.choice(
            status_weights
        )

        record = DemoRequest(

            name=fake.name(),

            institution_name=
            f"{random.choice(institutions)} "
            f"{fake.city()}",

            email=fake.email(),

            mobile=fake.msisdn()[:10],

            institution_type=institution_type,

            student_strength=random.randint(
                100,
                25000
            ),

            message=random.choice([
                "Interested in complete ERP solution.",
                "Need attendance and examination module.",
                "Looking for AI analytics dashboard.",
                "Require fee management system.",
                "Need multi-campus support.",
                "Interested in parent mobile app.",
                "Want migration from existing ERP.",
                "Need demo for school management.",
            ]),

            status=status,
        )

        data.append(record)

    DemoRequest.objects.bulk_create(
        data,
        batch_size=500
    )

    print(
        f"Successfully created "
        f"{TOTAL_RECORDS} demo requests."
    )

    print(
        f"Total Records : "
        f"{DemoRequest.objects.count()}"
    )


if __name__ == "__main__":

    create_demo_requests()