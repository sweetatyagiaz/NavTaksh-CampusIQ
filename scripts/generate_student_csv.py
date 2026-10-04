import pandas as pd
import random
from faker import Faker
from datetime import date
from django.utils.text import slugify

fake = Faker("en_IN")

TOTAL = 100000

rows = []

for i in range(1, TOTAL + 1):

    gender = random.choice([1, 2])

    dob = fake.date_between(
        start_date="-18y",
        end_date="-5y"
    )

    admission_date = fake.date_between(
        start_date="-5y",
        end_date="today"
    )

    rows.append({

        # "slug": slugify(f"STU{i:06d}"),
        "slug": f"stu{i:06d}",

        "admission_number": f"STU{i:06d}",

        "first_name": fake.first_name(),

        "middle_name": "",

        "last_name": fake.last_name(),

        "gender": gender,

        "date_of_birth": dob,

        "aadhaar_number": str(
            random.randint(
                100000000000,
                999999999999
            )
        ),

        "email": f"student{i}@campusiq.demo",

        "mobile": f"9{random.randint(100000000,999999999)}",

        "address_line_1": fake.street_address(),

        "city": fake.city(),

        "state": fake.state(),

        "country": "India",

        "postal_code": fake.postcode(),

        "admission_date": admission_date,

        "is_active": 1
    })

    if i % 10000 == 0:
        print(f"{i} generated")

data = pd.DataFrame(rows)

data.to_csv(
    "students_100000.csv",
    index=False
)

print("Done")