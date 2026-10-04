import pandas as pd

from django.core.management.base import BaseCommand

from apps.hr.models import Designation


class Command(BaseCommand):

    help = "Import Designations"

    def add_arguments(self, parser):

        parser.add_argument(
            "csv_file",
            type=str
        )

    def handle(self, *args, **options):

        data = pd.read_csv(
            options["csv_file"]
        )

        designations = []

        for _, row in data.iterrows():

            designations.append(

                Designation(

                    slug=row["slug"],
                    code=row["code"],
                    name=row["name"],
                    description=row["description"],
                    # is_active=row["is_active"]
                )
            )

        Designation.objects.bulk_create(
            designations,
            ignore_conflicts=True
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"{len(designations)} designations imported"
            )
        )