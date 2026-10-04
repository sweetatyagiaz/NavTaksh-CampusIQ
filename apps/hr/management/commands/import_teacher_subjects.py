import pandas as pd

from django.core.management.base import BaseCommand

from apps.hr.models import TeacherSubject


class Command(BaseCommand):

    help = "Import Teacher Subjects"

    def add_arguments(self, parser):

        parser.add_argument(
            "csv_file",
            type=str
        )

    def handle(self, *args, **options):

        data = pd.read_csv(
            options["csv_file"]
        )

        records = []

        batch_size = 5000

        total = 0

        for _, row in data.iterrows():

            records.append(

                TeacherSubject(

                    slug=row["slug"],

                    employment_id=int(
                        row["employment_id"]
                    ),

                    subject_id=int(
                        row["subject_id"]
                    ),

                    is_primary=bool(
                        row["is_primary"]
                    ),

                    remarks=str(
                        row["remarks"]
                    )
                    if pd.notna(
                        row["remarks"]
                    )
                    else ""
                )
            )

            if len(records) >= batch_size:

                TeacherSubject.objects.bulk_create(
                    records,
                    batch_size=batch_size,
                    ignore_conflicts=True
                )

                total += len(records)

                print(
                    f"{total} imported"
                )

                records = []

        if records:

            TeacherSubject.objects.bulk_create(
                records,
                batch_size=batch_size,
                ignore_conflicts=True
            )

            total += len(records)

        self.stdout.write(
            self.style.SUCCESS(
                f"{total} teacher subjects imported"
            )
        )