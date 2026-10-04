from django.db import models

from apps.core.models import BaseModel

class AcademicYear(models.Model):
    """
    Academic Year Master

    Example:

    Start Date : 2026-04-01
    End Date   : 2027-03-31

    Display    : 2026-2027
    """

    start_date = models.DateField(
        unique=True
    )

    end_date = models.DateField(
        unique=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "academic_year"
        ordering = ["-start_date"]
        verbose_name = "Academic Year"
        verbose_name_plural = "Academic Years"

    @property
    def name(self):
        return f"{self.start_date.year}-{self.end_date.year}"

    def __str__(self):
        return self.name

class Subject(BaseModel):

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
        db_table = "subject"

    def get_slug_source(self):
        return self.name

    def __str__(self):
        return self.name

class TeacherSubject(BaseModel):

    employment = models.ForeignKey(
        "hr.Employment",
        on_delete=models.CASCADE,
        related_name="teacher_subjects"
    )

    subject = models.ForeignKey(
        "academics.Subject",
        on_delete=models.PROTECT,
        related_name="teachers"
    )

    is_primary = models.BooleanField(
        default=False,
        help_text="Primary subject specialization"
    )

    start_date = models.DateField(
        null=True,
        blank=True
    )

    end_date = models.DateField(
        null=True,
        blank=True
    )

    remarks = models.TextField(
        blank=True
    )

    class Meta:
        db_table = "teacher_subject"

        constraints = [
            models.UniqueConstraint(
                fields=[
                    "employment",
                    "subject"
                ],
                name="unique_teacher_subject"
            )
        ]

    def get_slug_source(self):
        return (
            f"{self.employment.employee_code}-"
            f"{self.subject.name}"
        )

    def __str__(self):
        return (
            f"{self.employment.person} - "
            f"{self.subject.name}"
        )


