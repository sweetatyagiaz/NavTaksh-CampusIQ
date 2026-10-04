import pandas as pd

from django.core.management.base import BaseCommand

from apps.students.models import Student


class Command(BaseCommand):

    help = "Import Students"

    def add_arguments(self, parser):

        parser.add_argument(
            "csv_file",
            type=str
        )

    def handle(self, *args, **options):

        data = pd.read_csv(
            options["csv_file"]
        )

        students = []

        batch_size = 5000

        total = 0

        for _, row in data.iterrows():

            students.append(

                Student(
                    slug=row["slug"].lower(),

                    admission_number=row["admission_number"],

                    first_name=row["first_name"],

                    middle_name=row["middle_name"],

                    last_name=row["last_name"],

                    gender=row["gender"],

                    date_of_birth=row["date_of_birth"],

                    aadhaar_number=str(
                        row["aadhaar_number"]
                    ),

                    email=row["email"],

                    mobile=str(
                        row["mobile"]
                    ),

                    address_line_1=row["address_line_1"],

                    city=row["city"],

                    state=row["state"],

                    country=row["country"],

                    postal_code=str(
                        row["postal_code"]
                    ),

                    admission_date=row["admission_date"],

                    is_active=row["is_active"]
                )
            )

            if len(students) >= batch_size:

                Student.objects.bulk_create(
                    students,
                    batch_size=batch_size
                )

                total += len(students)

                print(
                    f"{total} imported"
                )

                students = []

        if students:

            Student.objects.bulk_create(
                students,
                batch_size=batch_size
            )

            total += len(students)

        self.stdout.write(
            self.style.SUCCESS(
                f"{total} students imported"
            )
        )