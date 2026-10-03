from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group


ROLES = [
    "SUPER_ADMIN",
    "SCHOOL_ADMIN",
    "PRINCIPAL",
    "TEACHER",
    "PARENT",
    "STUDENT",
    "ACCOUNTANT",
    "LIBRARIAN",
    "TRANSPORT_MANAGER",
]


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        for role in ROLES:
            Group.objects.get_or_create(name=role)

        self.stdout.write(
            self.style.SUCCESS("Roles created")
        )