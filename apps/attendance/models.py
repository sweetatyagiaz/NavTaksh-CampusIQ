from django.db import models

# Create your models here.

class AttendanceStatus(models.TextChoices):

    PRESENT = "PRESENT", "Present"
    ABSENT = "ABSENT", "Absent"
    LEAVE = "LEAVE", "Leave"
    HALF_DAY = "HALF_DAY", "Half Day"

class StudentAttendance(models.Model):

    student = models.ForeignKey(
        "students.Student",
        on_delete=models.CASCADE
    )

    attendance_date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=AttendanceStatus.choices
    )

    remarks = models.CharField(
        max_length=255,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        unique_together = (
            "student",
            "attendance_date"
        )

