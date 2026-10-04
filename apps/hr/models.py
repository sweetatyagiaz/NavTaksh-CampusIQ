from django.db import models

from apps.core.models import BaseModel
from apps.core.constants import Gender


class Department(BaseModel):

    code = models.CharField(
        max_length=20,
        help_text="Unique department code within a school"
    )

    name = models.CharField(
        max_length=100
    )

    description = models.TextField(
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    class Meta:
        db_table = "department"

        ordering = [
            "name"
        ]

    def get_slug_source(self):
        return self.code

    def __str__(self):
        return self.name


class Designation(BaseModel):

    code = models.CharField(
        max_length=20,
        unique=True
    )

    name = models.CharField(
        max_length=255,
        unique=True
    )

    description = models.TextField(
        blank=True
    )

    is_teaching_staff = models.BooleanField(
        default=False
    )
    class Meta:
        db_table = "designation"
        ordering = ["name"]

    def get_slug_source(self):
        return self.name

    def __str__(self):
        return self.name

class Employee(BaseModel):

    class Status(models.IntegerChoices):
        ACTIVE = 1, "Active"
        ON_LEAVE = 2, "On Leave"
        SUSPENDED = 3, "Suspended"
        RESIGNED = 4, "Resigned"
        RETIRED = 5, "Retired"
        TERMINATED = 6, "Terminated"

    person = models.ForeignKey(
        "people.Person",
        on_delete=models.PROTECT,
        related_name="employees"
    )

    school = models.ForeignKey(
        "organizations.School",
        on_delete=models.PROTECT,
        related_name="employees"
    )

    department = models.ForeignKey(
        "hr.Department",
        on_delete=models.PROTECT,
        related_name="employees"
    )

    designation = models.ForeignKey(
        "hr.Designation",
        on_delete=models.PROTECT,
        related_name="employees"
    )

    employee_code = models.CharField(
        max_length=50
    )

    joining_date = models.DateField()

    status = models.PositiveSmallIntegerField(
        choices=Status.choices,
        default=Status.ACTIVE
    )

    class Meta:
        db_table = "employee"

        unique_together = (
            "school",
            "employee_code"
        )

        ordering = [
            "employee_code"
        ]

    def get_slug_source(self):
        return (
            f"{self.employee_code}-"
            f"{self.person}"
        )

    def __str__(self):
        return (
            f"{self.employee_code} - "
            f"{self.person}"
        )


class EmployeeResignation(BaseModel):

    class Reason(models.IntegerChoices):
        RESIGNED = 1, "Resigned"
        RETIRED = 2, "Retired"
        TERMINATED = 3, "Terminated"
        CONTRACT_ENDED = 4, "Contract Ended"
        DECEASED = 5, "Deceased"
        TRANSFERRED = 6, "Transferred"

    employee = models.OneToOneField(
        "hr.Employee",
        on_delete=models.CASCADE,
        related_name="resignation"
    )

    reason = models.PositiveSmallIntegerField(
        choices=Reason.choices
    )

    resignation_date = models.DateField()

    last_working_date = models.DateField()

    reason_details = models.TextField(
        blank=True,
        help_text="Detailed explanation"
    )

    relieving_letter = models.FileField(
        upload_to="hr/resignations/",
        blank=True,
        null=True
    )

    exit_interview_notes = models.TextField(
        blank=True
    )

    is_rehire_eligible = models.BooleanField(
        default=True
    )

    remarks = models.TextField(
        blank=True
    )

    class Meta:
        db_table = "employee_resignation"

        ordering = [
            "-last_working_date"
        ]

    def get_slug_source(self):
        return (
            f"{self.employee.employee_code}-"
            f"{self.employee.person}"
        )

    def __str__(self):
        return (
            f"{self.employee.employee_code}"
        )

