from django.core.management.base import BaseCommand

from apps.organizations.models import Board


class Command(BaseCommand):

    help = "Import boards"

    def handle(self, *args, **kwargs):

        boards = [
            ("CBSE", "Central Board of Secondary Education"),
            ("ICSE", "Indian Certificate of Secondary Education"),
            ("ISC", "Indian School Certificate"),
            ("NIOS", "National Institute of Open Schooling"),
            ("IB", "International Baccalaureate"),
            ("IGCSE", "International General Certificate of Secondary Education"),
            ("CISCE", "Council for the Indian School Certificate Examinations"),
            ("HBSE", "Haryana Board of School Education"),
            ("UPMSP", "Uttar Pradesh Madhyamik Shiksha Parishad"),
            ("RBSE", "Board of Secondary Education Rajasthan"),
        ]

        for code, name in boards:

            Board.objects.get_or_create(
                code=code,
                defaults={
                    "name": name
                }
            )

        self.stdout.write(
            self.style.SUCCESS(
                "Boards imported successfully"
            )
        )