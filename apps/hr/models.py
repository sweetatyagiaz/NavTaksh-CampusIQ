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

    school = models.ForeignKey(
        "organizations.School",
        on_delete=models.CASCADE,
        related_name="departments"
    )

    is_active = models.BooleanField(
        default=True
    )

    class Meta:
        db_table = "department"

        ordering = [
            "name"
        ]

        constraints = [
            models.UniqueConstraint(
                fields=[
                    "school",
                    "code"
                ],
                name="uq_department_school_code"
            ),
            models.UniqueConstraint(
                fields=[
                    "school",
                    "name"
                ],
                name="uq_department_school_name"
            )
        ]

    def get_slug_source(self):
        return f"{self.school_id}-{self.code}"

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

    class Meta:
        db_table = "designation"
        ordering = ["name"]

    def get_slug_source(self):
        return self.name

    def __str__(self):
        return self.name


class Employment(BaseModel):

    person = models.ForeignKey(
        # Person,
        "people.Person",
        on_delete=models.PROTECT,
        related_name="employments"
    )

    school = models.ForeignKey(
        "organizations.School",
        on_delete=models.PROTECT,
        related_name="employments"
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        related_name="employments",
        null=True,
        blank=True
    )

    designation = models.ForeignKey(
        Designation,
        on_delete=models.PROTECT,
        related_name="employments"
    )

    employee_code = models.CharField(
        max_length=50
    )

    joining_date = models.DateField()

    relieving_date = models.DateField(
        null=True,
        blank=True
    )

    is_current = models.BooleanField(
        default=True
    )

    class Meta:
        db_table = "employment"

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


class Resignation(BaseModel):
    """
    Employee resignation / separation record.
    """

    class ReasonType(models.IntegerChoices):
        RESIGNED = 1, "Resigned"
        RETIRED = 2, "Retired"
        TERMINATED = 3, "Terminated"
        CONTRACT_ENDED = 4, "Contract Ended"
        TRANSFERRED = 5, "Transferred"
        DECEASED = 6, "Deceased"
        ABSCONDED = 7, "Absconded"
        OTHER = 99, "Other"

    employment = models.OneToOneField(
        "hr.Employment",
        on_delete=models.CASCADE,
        related_name="resignation"
    )

    reason_type = models.CharField(
        max_length=30,
        choices=ReasonType.choices
    )

    resignation_date = models.DateField(
        help_text="Last working day"
    )

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

    class Meta:
        db_table = "resignation"
        ordering = ["-resignation_date"]

    def get_slug_source(self):
        return (
            f"{self.employment.employee_code}-"
            f"{self.reason_type}"
        )

    def __str__(self):
        return (
            f"{self.employment.employee_code} - "
            f"{self.reason_type}"
        )


class TeacherSubject(BaseModel):

    employment = models.ForeignKey(
        "hr.Employment",
        on_delete=models.CASCADE,
        related_name="subjects"
    )

    subject = models.ForeignKey(
        "academics.Subject",
        on_delete=models.PROTECT,
        related_name="teachers"
    )

    is_primary = models.BooleanField(
        default=False,
        help_text="Primary subject of the teacher"
    )

    remarks = models.TextField(
        blank=True
    )

    class Meta:
        db_table = "teacher_subject"

        ordering = [
            "employment",
            "subject"
        ]

        constraints = [
            models.UniqueConstraint(
                fields=[
                    "employment",
                    "subject"
                ],
                name="uq_teacher_subject"
            )
        ]

    def get_slug_source(self):
        return (
            f"{self.employment_id}-"
            f"{self.subject_id}"
        )

    def __str__(self):
        return (
            f"{self.employment} - "
            f"{self.subject}"
        )