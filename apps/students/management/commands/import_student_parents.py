import pandas as pd

from django.core.management.base import BaseCommand

from apps.students.models import (
    Student,
    StudentParent
)

from apps.people.models import Person


class Command(BaseCommand):

    help = "Import Student Parents"

    def add_arguments(self, parser):

        parser.add_argument(
            "csv_file",
            type=str
        )

    def handle(self, *args, **options):

        data = pd.read_csv(
            options["csv_file"]
        )

        relationships = []

        batch_size = 5000

        total = 0

        for _, row in data.iterrows():

            relationships.append(

                StudentParent(

                    slug=(
                        f"sp-"
                        f"{row['student_id']}-"
                        f"{row['person_id']}-"
                        f"{row['relationship_type']}"
                    ),

                    student_id=int(
                        row["student_id"]
                    ),

                    person_id=int(
                        row["person_id"]
                    ),

                    relationship_type=int(
                        row["relationship_type"]
                    ),

                    is_primary_contact=bool(
                        row["is_primary_contact"]
                    ),

                    can_pickup_student=bool(
                        row["can_pickup_student"]
                    ),

                    receives_sms=bool(
                        row["receives_sms"]
                    ),

                    receives_whatsapp=bool(
                        row["receives_whatsapp"]
                    ),

                    receives_email=bool(
                        row["receives_email"]
                    ),

                    remarks=row["remarks"]
                )
            )

            if len(relationships) >= batch_size:

                StudentParent.objects.bulk_create(
                    relationships,
                    batch_size=batch_size,
                    ignore_conflicts=True
                )

                total += len(
                    relationships
                )

                print(
                    f"{total} imported"
                )

                relationships = []

        if relationships:

            StudentParent.objects.bulk_create(
                relationships,
                batch_size=batch_size,
                ignore_conflicts=True
            )

            total += len(
                relationships
            )

        self.stdout.write(
            self.style.SUCCESS(
                f"{total} relationships imported"
            )
        )