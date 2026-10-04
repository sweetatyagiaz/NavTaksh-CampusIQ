import pandas as pd

from django.core.management.base import BaseCommand

from apps.people.models import Person


class Command(BaseCommand):

    help = "Import persons"

    def add_arguments(self, parser):

        parser.add_argument(
            "csv_file",
            type=str
        )

    def handle(self, *args, **options):

        data = pd.read_csv(
            options["csv_file"]
        )

        imported = 0

        for _, row in data.iterrows():

            Person.objects.create(
                aadhaar_number=str(
                    row["aadhaar_number"]
                ),
                aadhaar_verified=bool(
                    row["aadhaar_verified"]
                ),
                first_name=row["first_name"],
                middle_name=""
                if pd.isna(
                    row["middle_name"]
                )
                else row["middle_name"],
                last_name=""
                if pd.isna(
                    row["last_name"]
                )
                else row["last_name"],
                email=""
                if pd.isna(
                    row["email"]
                )
                else row["email"],
                mobile=str(
                    row["mobile"]
                ),
                alternate_mobile=""
                if pd.isna(
                    row["alternate_mobile"]
                )
                else str(
                    row["alternate_mobile"]
                ),
                date_of_birth=row[
                    "date_of_birth"
                ],
                gender=int(
                    row["gender"]
                ),
                address_line_1=row[
                    "address_line_1"
                ],
                city=row["city"],
                state=row["state"],
                country=row["country"],
                postal_code=str(
                    row["postal_code"]
                ),
                is_active=bool(
                    row["is_active"]
                )
            )

            imported += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"{imported} persons imported"
            )
        )