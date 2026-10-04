import pandas as pd

from django.core.management.base import BaseCommand

from apps.hr.models import Resignation


class Command(BaseCommand):

    help = "Import Resignations"

    def add_arguments(self, parser):

        parser.add_argument(
            "csv_file",
            type=str
        )

    def handle(self, *args, **options):

        data = pd.read_csv(
            options["csv_file"]
        )

        resignations = []

        batch_size = 5000

        total = 0

        for _, row in data.iterrows():

            resignations.append(

                Resignation(

                    slug=row["slug"],

                    employment_id=int(
                        row["employment_id"]
                    ),

                    reason_type=int(
                        row["reason_type"]
                    ),

                    resignation_date=row[
                        "resignation_date"
                    ],

                    reason_details=row[
                        "reason_details"
                    ],

                    exit_interview_notes=row[
                        "exit_interview_notes"
                    ],

                    is_rehire_eligible=bool(
                        row[
                            "is_rehire_eligible"
                        ]
                    )
                )
            )

            if len(resignations) >= batch_size:

                Resignation.objects.bulk_create(
                    resignations,
                    batch_size=batch_size,
                    ignore_conflicts=True
                )

                total += len(
                    resignations
                )

                print(
                    f"{total} imported"
                )

                resignations = []

        if resignations:

            Resignation.objects.bulk_create(
                resignations,
                batch_size=batch_size,
                ignore_conflicts=True
            )

            total += len(
                resignations
            )

        self.stdout.write(
            self.style.SUCCESS(
                f"{total} resignations imported"
            )
        )