import pandas as pd

from django.core.management.base import BaseCommand

from apps.people.models import (
    Person,
    PersonAddress
)


class Command(BaseCommand):

    help = "Import person addresses from CSV"

    def add_arguments(self, parser):

        parser.add_argument(
            "csv_file",
            type=str
        )

    def handle(self, *args, **options):

        csv_file = options["csv_file"]

        data = pd.read_csv(csv_file)

        imported = 0

        for _, row in data.iterrows():

            try:

                person = Person.objects.get(
                    id=int(row["person_id"])
                )

                PersonAddress.objects.create(
                    person=person,

                    address_type=int(
                        row["address_type"]
                    ),

                    address_line_1=row[
                        "address_line_1"
                    ],

                    address_line_2=""
                    if pd.isna(
                        row["address_line_2"]
                    )
                    else row[
                        "address_line_2"
                    ],

                    landmark=""
                    if pd.isna(
                        row["landmark"]
                    )
                    else row[
                        "landmark"
                    ],

                    city=row["city"],

                    district=""
                    if pd.isna(
                        row["district"]
                    )
                    else row["district"],

                    state=row["state"],

                    country=row["country"],

                    postal_code=str(
                        row["postal_code"]
                    ),

                    latitude=None
                    if pd.isna(
                        row["latitude"]
                    )
                    else row["latitude"],

                    longitude=None
                    if pd.isna(
                        row["longitude"]
                    )
                    else row["longitude"],

                    is_primary=bool(
                        row["is_primary"]
                    ),

                    remarks=""
                    if pd.isna(
                        row["remarks"]
                    )
                    else row["remarks"]
                )

                imported += 1

            except Exception as e:

                self.stdout.write(
                    self.style.WARNING(
                        f"Skipped row: {e}"
                    )
                )

        self.stdout.write(
            self.style.SUCCESS(
                f"{imported} addresses imported"
            )
        )