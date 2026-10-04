from django.db import models

from apps.core.models import BaseModel
from apps.core.constants import Gender


class Student(BaseModel):

    admission_number = models.CharField(
        max_length=50,
        unique=True,
        db_index=True
    )

    first_name = models.CharField(
        max_length=100
    )

    middle_name = models.CharField(
        max_length=100,
        blank=True
    )

    last_name = models.CharField(
        max_length=100,
        blank=True
    )

    gender = models.PositiveSmallIntegerField(
        choices=Gender.choices,
        default=Gender.NOT_AVAILABLE,
        db_index=True
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True
    )

    aadhaar_number = models.CharField(
        max_length=12,
        blank=True,
        null=True,
        unique=True
    )

    email = models.EmailField(
        blank=True
    )

    mobile = models.CharField(
        max_length=20,
        blank=True
    )

    profile_photo = models.ImageField(
        upload_to="students/photos/",
        blank=True,
        null=True
    )

    address_line_1 = models.CharField(
        max_length=255,
        blank=True
    )

    city = models.CharField(
        max_length=100,
        blank=True
    )

    state = models.CharField(
        max_length=100,
        blank=True
    )

    country = models.CharField(
        max_length=100,
        default="India"
    )

    postal_code = models.CharField(
        max_length=20,
        blank=True
    )

    admission_date = models.DateField(
        null=True,
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    class Meta:
        db_table = "student"
        ordering = ["admission_number"]

    def get_slug_source(self):
        return self.admission_number

    def __str__(self):
        return (
            f"{self.admission_number} - "
            f"{self.first_name} {self.last_name}"
        )


class StudentParent(BaseModel):

    class RelationshipType(models.IntegerChoices):
        FATHER = 1, "Father"
        MOTHER = 2, "Mother"
        GUARDIAN = 3, "Guardian"
        GRANDPARENT = 4, "Grandparent"
        OTHER = 99, "Other"

    student = models.ForeignKey(
        "students.Student",
        on_delete=models.CASCADE,
        related_name="parents"
    )

    person = models.ForeignKey(
        "people.Person",
        on_delete=models.PROTECT,
        related_name="student_relationships"
    )

    relationship_type = models.PositiveSmallIntegerField(
        choices=RelationshipType.choices,
        db_index=True
    )

    is_primary_contact = models.BooleanField(
        default=False
    )

    can_pickup_student = models.BooleanField(
        default=True
    )

    receives_sms = models.BooleanField(
        default=True
    )

    receives_whatsapp = models.BooleanField(
        default=True
    )

    receives_email = models.BooleanField(
        default=True
    )

    remarks = models.TextField(
        blank=True
    )

    class Meta:
        db_table = "student_parent"

        constraints = [
            models.UniqueConstraint(
                fields=[
                    "student",
                    "person",
                    "relationship_type"
                ],
                name="unique_student_parent"
            )
        ]

    def get_slug_source(self):
        return (
            f"{self.student.admission_number}-"
            f"{self.person.id}"
        )

    def __str__(self):
        return (
            f"{self.student} - "
            f"{self.relationship_type}"
        )

