import pandas as pd

from django.core.management.base import BaseCommand

from apps.people.models import (
    Person,
    PersonContact
)


class Command(BaseCommand):

    help = "Import Person Contacts"

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

                PersonContact.objects.create(
                    person=person,

                    contact_type=int(
                        row["contact_type"]
                    ),

                    value=str(
                        row["value"]
                    ),

                    is_primary=bool(
                        row["is_primary"]
                    ),

                    is_verified=bool(
                        row["is_verified"]
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
                f"{imported} contacts imported"
            )
        )