from django.core.management.base import BaseCommand

from apps.accounts.models import (
    Role,
    Permission,
    RolePermission
)


class Command(BaseCommand):

    help = "Assign permissions to roles"

    ROLE_PERMISSIONS = {

        "SUPER_ADMIN": ["*"],

        "PLATFORM_ADMIN": [
            "*"
        ],

        "SCHOOL_ADMIN": [
            "USER_VIEW",
            "USER_CREATE",
            "USER_UPDATE",

            "ROLE_VIEW",
            "ROLE_ASSIGN",

            "STUDENT_VIEW",
            "STUDENT_CREATE",
            "STUDENT_UPDATE",
            "STUDENT_DELETE",

            "TEACHER_VIEW",
            "TEACHER_CREATE",
            "TEACHER_UPDATE",

            "ATTENDANCE_VIEW",
            "ATTENDANCE_MARK",

            "EXAM_VIEW",
            "EXAM_CREATE",
            "EXAM_UPDATE",
            "EXAM_PUBLISH",

            "MARKS_VIEW",
            "MARKS_ENTRY",
            "MARKS_UPDATE",

            "FEE_VIEW",
            "FEE_COLLECT",
            "FEE_REPORT",

            "LIBRARY_VIEW",

            "TRANSPORT_VIEW",
            "TRANSPORT_MANAGE",

            "HOSTEL_VIEW",
            "HOSTEL_MANAGE",

            "HR_VIEW",

            "REPORT_VIEW",
            "REPORT_EXPORT",

            "ANALYTICS_VIEW",

            "COMMUNICATION_VIEW",
            "COMMUNICATION_SEND",
        ],

        "PRINCIPAL": [
            "STUDENT_VIEW",
            "TEACHER_VIEW",
            "ATTENDANCE_VIEW",
            "EXAM_VIEW",
            "MARKS_VIEW",
            "REPORT_VIEW",
            "ANALYTICS_VIEW",
        ],

        "TEACHER": [
            "STUDENT_VIEW",
            "ATTENDANCE_VIEW",
            "ATTENDANCE_MARK",
            "EXAM_VIEW",
            "MARKS_VIEW",
            "MARKS_ENTRY",
            "MARKS_UPDATE",
        ],

        "ACCOUNTANT": [
            "FEE_VIEW",
            "FEE_COLLECT",
            "FEE_REFUND",
            "FEE_REPORT",
        ],

        "LIBRARIAN": [
            "LIBRARY_VIEW",
            "LIBRARY_BOOK_ISSUE",
            "LIBRARY_BOOK_RETURN",
        ],

        "HR_MANAGER": [
            "HR_VIEW",
            "HR_CREATE",
            "HR_UPDATE",
        ],

        "PARENT": [
            "STUDENT_VIEW",
            "ATTENDANCE_VIEW",
            "MARKS_VIEW",
            "FEE_VIEW",
        ],

        "STUDENT": [
            "ATTENDANCE_VIEW",
            "MARKS_VIEW",
        ]
    }

    def handle(self, *args, **kwargs):

        created_count = 0

        for role_code, permission_codes in self.ROLE_PERMISSIONS.items():

            try:
                role = Role.objects.get(code=role_code)

            except Role.DoesNotExist:
                self.stdout.write(
                    self.style.WARNING(
                        f"Role not found: {role_code}"
                    )
                )
                continue

            if "*" in permission_codes:

                permissions = Permission.objects.all()

            else:

                permissions = Permission.objects.filter(
                    code__in=permission_codes
                )

            for permission in permissions:

                _, created = RolePermission.objects.get_or_create(
                    role=role,
                    permission=permission
                )

                if created:
                    created_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"{created_count} role permissions created."
            )
        )