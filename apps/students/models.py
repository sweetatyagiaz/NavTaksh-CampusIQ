from django.db import models

from apps.core.models import BaseModel
# from apps.core.constants import Gender


class Student(BaseModel):

    class Status(models.IntegerChoices):
        ACTIVE = 1, "Active"
        TRANSFERRED = 2, "Transferred"
        PASSED_OUT = 3, "Passed Out"
        DROPPED = 4, "Dropped"
        SUSPENDED = 5, "Suspended"
        ALUMNI = 6, "Alumni"

    person = models.ForeignKey(
        "people.Person",
        on_delete=models.PROTECT,
        related_name="students"
    )

    school = models.ForeignKey(
        "organizations.School",
        on_delete=models.PROTECT,
        related_name="students"
    )

    admission_number = models.CharField(
        max_length=50
    )

    admission_date = models.DateField()

    status = models.PositiveSmallIntegerField(
        choices=Status.choices,
        default=Status.ACTIVE
    )

    class Meta:

        db_table = "student"

        unique_together = (
            "school",
            "admission_number"
        )

        ordering = [
            "admission_number"
        ]

    def get_slug_source(self):
        return (
            f"{self.admission_number}-"
            f"{self.person}"
        )

    def __str__(self):
        return (
            f"{self.admission_number} - "
            f"{self.person}"
        )

class StudentEnrollment(BaseModel):
    class EnrollmentStatus(models.IntegerChoices):
        ACTIVE = 1, "Active"
        PROMOTED = 2, "Promoted"
        DETAINED = 3, "Detained"
        TRANSFERRED = 4, "Transferred"
        PASSED_OUT = 5, "Passed Out"
        DROPPED = 6, "Dropped"

    student = models.ForeignKey(
        "students.Student",
        on_delete=models.CASCADE,
        related_name="enrollments"
    )

    class_section = models.ForeignKey(
        "academics.ClassSection",
        on_delete=models.PROTECT,
        related_name="enrollments"
    )

    roll_number = models.PositiveIntegerField()

    enrollment_date = models.DateField()

    status = models.PositiveSmallIntegerField(
        choices=EnrollmentStatus.choices,
        default=EnrollmentStatus.ACTIVE
    )

    class Meta:

        db_table = "student_enrollment"

        unique_together = (
            "class_section",
            "roll_number"
        )

    def get_slug_source(self):
        return (
            f"{self.student}-"
            f"{self.class_section}"
        )
    
class StudentGuardian(BaseModel):

    class Relationship(models.IntegerChoices):
        FATHER = 1, "Father"
        MOTHER = 2, "Mother"
        GUARDIAN = 3, "Guardian"
        GRAND_FATHER = 4, "Grand Father"
        GRAND_MOTHER = 5, "Grand Mother"
        UNCLE = 6, "Uncle"
        AUNT = 7, "Aunt"
        OTHER = 8, "Other"

    student = models.ForeignKey(
        "students.Student",
        on_delete=models.CASCADE,
        related_name="guardians"
    )

    person = models.ForeignKey(
        "people.Person",
        on_delete=models.PROTECT,
        related_name="guardian_students"
    )

    relationship = models.PositiveSmallIntegerField(
        choices=Relationship.choices
    )

    is_primary = models.BooleanField(
        default=False
    )

    can_pickup_student = models.BooleanField(
        default=True
    )

    is_emergency_contact = models.BooleanField(
        default=False
    )

    class Meta:
        db_table = "student_guardian"

    def get_slug_source(self):
        return (
            f"{self.student}-"
            f"{self.person}"
        )

class StudentDocument(BaseModel):

    student = models.ForeignKey(
        "students.Student",
        on_delete=models.CASCADE,
        related_name="documents"
    )

    document_type = models.CharField(
        max_length=100
    )

    document_number = models.CharField(
        max_length=100,
        blank=True
    )

    file = models.FileField(
        upload_to="students/documents/"
    )

    issue_date = models.DateField(
        null=True,
        blank=True
    )

    expiry_date = models.DateField(
        null=True,
        blank=True
    )

    remarks = models.TextField(
        blank=True
    )

    class Meta:
        db_table = "student_document"

    def get_slug_source(self):
        return (
            f"{self.student}-"
            f"{self.document_type}"
        )



