import pandas as pd

from django.core.management.base import BaseCommand

from apps.hr.models import Employment


class Command(BaseCommand):

    help = "Import Employments"

    def add_arguments(self, parser):

        parser.add_argument(
            "csv_file",
            type=str
        )

    def handle(self, *args, **options):

        data = pd.read_csv(
            options["csv_file"]
        )

        employments = []

        batch_size = 5000

        total = 0

        for _, row in data.iterrows():

            employments.append(

                Employment(

                    slug=row["slug"],

                    person_id=int(
                        row["person_id"]
                    ),

                    school_id=int(
                        row["school_id"]
                    ),

                    department_id=int(
                        row["department_id"]
                    ),

                    designation_id=int(
                        row["designation_id"]
                    ),

                    employee_code=row[
                        "employee_code"
                    ],

                    joining_date=row[
                        "joining_date"
                    ],

                    relieving_date=(
                        None
                        if pd.isna(
                            row[
                                "relieving_date"
                            ]
                        )
                        else row[
                            "relieving_date"
                        ]
                    ),

                    is_current=bool(
                        row["is_current"]
                    )
                )
            )

            if len(employments) >= batch_size:

                Employment.objects.bulk_create(
                    employments,
                    batch_size=batch_size,
                    ignore_conflicts=True
                )

                total += len(
                    employments
                )

                print(
                    f"{total} imported"
                )

                employments = []

        if employments:

            Employment.objects.bulk_create(
                employments,
                batch_size=batch_size,
                ignore_conflicts=True
            )

            total += len(
                employments
            )

        self.stdout.write(
            self.style.SUCCESS(
                f"{total} employments imported"
            )
        )