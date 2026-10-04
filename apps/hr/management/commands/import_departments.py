import pandas as pd

from django.core.management.base import BaseCommand

from apps.hr.models import Department


class Command(BaseCommand):

    help = "Import Departments"

    def add_arguments(self, parser):

        parser.add_argument(
            "csv_file",
            type=str
        )

    def handle(self, *args, **options):

        data = pd.read_csv(
            options["csv_file"]
        )

        departments = []

        batch_size = 1000

        total = 0

        for _, row in data.iterrows():

            departments.append(

                Department(

                    slug=row["slug"],

                    code=row["code"],

                    name=row["name"],

                    description=row["description"],

                    is_active=bool(
                        row["is_active"]
                    )
                )
            )

            if len(departments) >= batch_size:

                Department.objects.bulk_create(
                    departments,
                    batch_size=batch_size,
                    ignore_conflicts=True
                )

                total += len(
                    departments
                )

                print(
                    f"{total} imported"
                )

                departments = []

        if departments:

            Department.objects.bulk_create(
                departments,
                batch_size=batch_size,
                ignore_conflicts=True
            )

            total += len(
                departments
            )

        self.stdout.write(
            self.style.SUCCESS(
                f"{total} departments imported"
            )
        )