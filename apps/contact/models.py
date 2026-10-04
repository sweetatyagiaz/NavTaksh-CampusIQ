from django.db import models


class DemoRequest(models.Model):

    class Status(models.IntegerChoices):
        NEW = 1, "New"
        CONTACTED = 2, "Contacted"
        QUALIFIED = 3, "Qualified"
        DEMO_SCHEDULED = 4, "Demo Scheduled"
        CONVERTED = 5, "Converted"
        REJECTED = 6, "Rejected"

    class InstitutionType(models.IntegerChoices):
        SCHOOL = 1, "School"
        COLLEGE = 2, "College"
        UNIVERSITY = 3, "University"
        COACHING = 4, "Coaching Institute"
        TRAINING = 5, "Training Center"

    name = models.CharField(
        max_length=255
    )

    institution_name = models.CharField(
        max_length=255
    )

    email = models.EmailField()

    mobile = models.CharField(
        max_length=20
    )

    institution_type = models.PositiveSmallIntegerField(
        choices=InstitutionType.choices
    )

    student_strength = models.PositiveIntegerField(
        blank=True,
        null=True
    )

    message = models.TextField(
        blank=True
    )

    status = models.PositiveSmallIntegerField(
        choices=Status.choices,
        default=Status.NEW
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        db_table = "demo_request"

        ordering = [
            "-created_at"
        ]

    def __str__(self):
        return f"{self.institution_name} - {self.name}"