import pandas as pd

from django.core.management.base import BaseCommand

from apps.organizations.models import (
    School,
    Board,
    SchoolBoardRegistration
)


class Command(BaseCommand):

    help = "Import School Board Registrations"

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

            try:

                school = School.objects.get(
                    id=row["school_id"]
                )

                board = Board.objects.get(
                    id=row["board_id"]
                )

                SchoolBoardRegistration.objects.create(
                    school=school,
                    board=board,
                    registration_number=row[
                        "registration_number"
                    ],
                    affiliation_number=row[
                        "affiliation_number"
                    ],
                    registration_date=row[
                        "registration_date"
                    ],
                    remarks=row[
                        "remarks"
                    ]
                )

                imported += 1

            except Exception as e:

                self.stdout.write(
                    self.style.WARNING(str(e))
                )

        self.stdout.write(
            self.style.SUCCESS(
                f"{imported} registrations imported"
            )
        )