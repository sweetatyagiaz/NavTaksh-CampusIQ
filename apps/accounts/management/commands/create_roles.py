from django.core.management.base import BaseCommand

from apps.accounts.models import Role


class Command(BaseCommand):

    help = "Create default roles"

    def handle(self, *args, **kwargs):

        roles = [

            # Platform Roles
            ("SUPER_ADMIN", "Super Admin", "PLATFORM"),
            ("PLATFORM_ADMIN", "Platform Admin", "PLATFORM"),
            ("SALES_MANAGER", "Sales Manager", "PLATFORM"),
            ("SUPPORT_ADMIN", "Support Admin", "PLATFORM"),
            ("IMPLEMENTATION_MANAGER", "Implementation Manager", "PLATFORM"),
            ("FINANCE_ADMIN", "Finance Admin", "PLATFORM"),
            ("AUDITOR", "Auditor", "PLATFORM"),

            # Institution Roles
            ("SCHOOL_ADMIN", "School Admin", "INSTITUTION"),
            ("PRINCIPAL", "Principal", "INSTITUTION"),
            ("VICE_PRINCIPAL", "Vice Principal", "INSTITUTION"),
            ("ACADEMIC_COORDINATOR", "Academic Coordinator", "INSTITUTION"),
            ("EXAM_CONTROLLER", "Exam Controller", "INSTITUTION"),
            ("DEPARTMENT_HEAD", "Department Head", "INSTITUTION"),
            ("TEACHER", "Teacher", "INSTITUTION"),
            ("COUNSELOR", "Counselor", "INSTITUTION"),
            ("ACCOUNTANT", "Accountant", "INSTITUTION"),
            ("LIBRARIAN", "Librarian", "INSTITUTION"),
            ("TRANSPORT_MANAGER", "Transport Manager", "INSTITUTION"),
            ("HOSTEL_WARDEN", "Hostel Warden", "INSTITUTION"),
            ("HR_MANAGER", "HR Manager", "INSTITUTION"),
            ("RECEPTIONIST", "Receptionist", "INSTITUTION"),
            ("SECURITY_OFFICER", "Security Officer", "INSTITUTION"),
            ("IT_ADMIN", "IT Administrator", "INSTITUTION"),

            ("STUDENT", "Student", "INSTITUTION"),
            ("PARENT", "Parent", "INSTITUTION"),
            ("ALUMNI", "Alumni", "INSTITUTION"),
        ]

        for code, name, role_type in roles:

            Role.objects.get_or_create(
                code=code,
                defaults={
                    "name": name,
                    "role_type": role_type,
                }
            )

        self.stdout.write(
            self.style.SUCCESS(
                "Roles created successfully."
            )
        )