import pandas as pd

from django.core.management.base import BaseCommand

from apps.organizations.models import School


class Command(BaseCommand):

    help = "Import schools from CSV"

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

                School.objects.update_or_create(
                    code=row["code"],
                    defaults={
                        "name": row["name"],
                        "short_name": row["short_name"],
                        "registration_number": row["registration_number"],
                        "affiliation_number": row["affiliation_number"],
                        "udise_code": str(row["udise_code"]),
                        "email": row["email"],
                        "phone": str(row["phone"]),
                        "address_line_1": "",
                        "city": row["city"],
                        "state": row["state"],
                        "country": row["country"],
                        "postal_code": str(row["postal_code"]),
                        "website": row["website"],
                        "is_active": bool(row["is_active"])
                    }
                )

                imported += 1

            except Exception as e:

                self.stdout.write(
                    self.style.WARNING(
                        f"Skipped {row['code']}: {e}"
                    )
                )

        self.stdout.write(
            self.style.SUCCESS(
                f"{imported} schools imported"
            )
        )