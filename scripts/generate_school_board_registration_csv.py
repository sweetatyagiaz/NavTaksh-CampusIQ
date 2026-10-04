import os
import sys
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

from apps.organizations.models import (
    School,
    Board
)

rows = []

cbse = Board.objects.get(code="CBSE")
icse = Board.objects.get(code="ICSE")
ib = Board.objects.get(code="IB")
igcse = Board.objects.get(code="IGCSE")

schools = School.objects.order_by("id")

for index, school in enumerate(schools, start=1):

    if index <= 20:
        board = cbse

    elif index <= 22:
        board = icse

    elif index <= 24:
        board = ib

    else:
        board = igcse

    rows.append({
        "school_id": school.id,
        "board_id": board.id,
        "registration_number": f"REG-{school.code}",
        "affiliation_number": f"AFF-{school.code}",
        "registration_date": "2024-04-01",
        "remarks": ""
    })

data = pd.DataFrame(rows)

data.to_csv(
    "school_board_registrations.csv",
    index=False
)

print(
    f"{len(data)} registrations generated"
)