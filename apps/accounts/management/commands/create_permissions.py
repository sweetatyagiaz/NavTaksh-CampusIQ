from django.core.management.base import BaseCommand

from apps.accounts.models import Permission


class Command(BaseCommand):

    help = "Create default permissions"

    def handle(self, *args, **kwargs):

        permissions = [

            # User Management
            ("USER_VIEW", "View Users", "USER"),
            ("USER_CREATE", "Create User", "USER"),
            ("USER_UPDATE", "Update User", "USER"),
            ("USER_DELETE", "Delete User", "USER"),

            # Role Management
            ("ROLE_VIEW", "View Roles", "ROLE"),
            ("ROLE_ASSIGN", "Assign Roles", "ROLE"),

            # School Management
            ("SCHOOL_VIEW", "View School", "SCHOOL"),
            ("SCHOOL_UPDATE", "Update School", "SCHOOL"),

            # Student Management
            ("STUDENT_VIEW", "View Students", "STUDENT"),
            ("STUDENT_CREATE", "Create Student", "STUDENT"),
            ("STUDENT_UPDATE", "Update Student", "STUDENT"),
            ("STUDENT_DELETE", "Delete Student", "STUDENT"),

            # Teacher Management
            ("TEACHER_VIEW", "View Teachers", "TEACHER"),
            ("TEACHER_CREATE", "Create Teacher", "TEACHER"),
            ("TEACHER_UPDATE", "Update Teacher", "TEACHER"),
            ("TEACHER_DELETE", "Delete Teacher", "TEACHER"),

            # Attendance
            ("ATTENDANCE_VIEW", "View Attendance", "ATTENDANCE"),
            ("ATTENDANCE_MARK", "Mark Attendance", "ATTENDANCE"),
            ("ATTENDANCE_UPDATE", "Update Attendance", "ATTENDANCE"),

            # Examination
            ("EXAM_VIEW", "View Exams", "EXAM"),
            ("EXAM_CREATE", "Create Exam", "EXAM"),
            ("EXAM_UPDATE", "Update Exam", "EXAM"),
            ("EXAM_DELETE", "Delete Exam", "EXAM"),
            ("EXAM_PUBLISH", "Publish Results", "EXAM"),

            # Marks
            ("MARKS_VIEW", "View Marks", "MARKS"),
            ("MARKS_ENTRY", "Enter Marks", "MARKS"),
            ("MARKS_UPDATE", "Update Marks", "MARKS"),
            ("MARKS_APPROVE", "Approve Marks", "MARKS"),

            # Fees
            ("FEE_VIEW", "View Fees", "FEE"),
            ("FEE_COLLECT", "Collect Fees", "FEE"),
            ("FEE_REFUND", "Refund Fees", "FEE"),
            ("FEE_REPORT", "Fee Reports", "FEE"),

            # Library
            ("LIBRARY_VIEW", "View Library", "LIBRARY"),
            ("LIBRARY_BOOK_ISSUE", "Issue Book", "LIBRARY"),
            ("LIBRARY_BOOK_RETURN", "Return Book", "LIBRARY"),

            # Transport
            ("TRANSPORT_VIEW", "View Transport", "TRANSPORT"),
            ("TRANSPORT_MANAGE", "Manage Transport", "TRANSPORT"),

            # Hostel
            ("HOSTEL_VIEW", "View Hostel", "HOSTEL"),
            ("HOSTEL_MANAGE", "Manage Hostel", "HOSTEL"),

            # HR
            ("HR_VIEW", "View Employees", "HR"),
            ("HR_CREATE", "Create Employee", "HR"),
            ("HR_UPDATE", "Update Employee", "HR"),

            # Reports
            ("REPORT_VIEW", "View Reports", "REPORT"),
            ("REPORT_EXPORT", "Export Reports", "REPORT"),

            # Analytics
            ("ANALYTICS_VIEW", "View Analytics", "ANALYTICS"),

            # Communication
            ("COMMUNICATION_VIEW", "View Messages", "COMMUNICATION"),
            ("COMMUNICATION_SEND", "Send Messages", "COMMUNICATION"),
        ]

        count = 0

        for code, name, module in permissions:

            _, created = Permission.objects.get_or_create(
                code=code,
                defaults={
                    "name": name,
                    "module": module
                }
            )

            if created:
                count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"{count} permissions created successfully."
            )
        )