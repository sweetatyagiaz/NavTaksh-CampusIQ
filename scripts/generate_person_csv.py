import random

import pandas as pd

from faker import Faker


fake = Faker("en_IN")

rows = []

for i in range(1000):

    gender = random.choice([1, 2])

    aadhaar = str(
        random.randint(
            100000000000,
            999999999999
        )
    )

    first_name = (
        fake.first_name_male()
        if gender == 1
        else fake.first_name_female()
    )

    rows.append({
        "aadhaar_number": aadhaar,
        "aadhaar_verified": random.choice([0, 1]),
        "first_name": first_name,
        "middle_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "mobile": fake.msisdn()[:10],
        "alternate_mobile": fake.msisdn()[:10],
        "date_of_birth": fake.date_between(
            start_date="-65y",
            end_date="-18y"
        ),
        "gender": gender,
        "address_line_1": fake.street_address(),
        "city": fake.city(),
        "state": fake.state(),
        "country": "India",
        "postal_code": fake.postcode(),
        "is_active": 1
    })

data = pd.DataFrame(rows)

data.to_csv(
    "persons.csv",
    index=False
)

print("Generated 1000 persons")