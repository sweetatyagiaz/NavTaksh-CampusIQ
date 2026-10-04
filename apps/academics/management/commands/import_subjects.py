import pandas as pd

from django.core.management.base import BaseCommand

from apps.academics.models import Subject


class Command(BaseCommand):

    help = "Import Subjects"

    def add_arguments(self, parser):

        parser.add_argument(
            "csv_file",
            type=str
        )

    def handle(self, *args, **options):

        data = pd.read_csv(
            options["csv_file"]
        )

        subjects = []

        for _, row in data.iterrows():

            subjects.append(

                Subject(

                    slug=row["slug"],

                    code=row["code"],

                    name=row["name"],

                    description=row["description"]
                )
            )

        Subject.objects.bulk_create(
            subjects,
            ignore_conflicts=True
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"{len(subjects)} subjects imported"
            )
        )