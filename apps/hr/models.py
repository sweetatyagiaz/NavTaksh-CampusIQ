from django.db import models

from apps.core.models import BaseModel
from apps.core.constants import Gender



class Person(BaseModel):
    """
    Person Master

    Represents any non-student person
    associated with a school.
    """

    aadhaar_number = models.CharField(
        max_length=12,
        unique=True,
        blank=True,
        null=True,
        db_index=True
    )

    aadhaar_verified = models.BooleanField(
        default=False
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

    # employee_code = models.CharField(
    #     max_length=50,
    #     unique=True,
    #     blank=True,
    #     null=True
    # )    

    email = models.EmailField(
        blank=True
    )

    mobile = models.CharField(
        max_length=20,
        db_index=True
    )

    alternate_mobile = models.CharField(
        max_length=20,
        blank=True
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True
    )

    # gender = models.CharField(
    #     max_length=20,
    #     blank=True
    # )
    gender = models.PositiveSmallIntegerField(
        choices=Gender.choices,
        default=Gender.NOT_AVAILABLE,
        null=True,
        blank=True,
        db_index=True
    )

    profile_photo = models.ImageField(
        upload_to="persons/photos/",
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

    is_active = models.BooleanField(
        default=True
    )

    class Meta:
        db_table = "person"
        ordering = [
            "first_name",
            "last_name"
        ]

    def get_slug_source(self):
        return (
            f"{self.first_name} "
            f"{self.last_name}"
        )

    def __str__(self):
        return (
            f"{self.first_name} "
            f"{self.last_name}"
        ).strip()


class Department(BaseModel):

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
        db_table = "department"
        ordering = ["name"]

    def get_slug_source(self):
        return self.name

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
        Person,
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

    class ReasonType(models.TextChoices):

        RESIGNED = "RESIGNED", "Resigned"

        RETIRED = "RETIRED", "Retired"

        TERMINATED = "TERMINATED", "Terminated"

        CONTRACT_ENDED = "CONTRACT_ENDED", "Contract Ended"

        TRANSFERRED = "TRANSFERRED", "Transferred"

        DECEASED = "DECEASED", "Deceased"

        ABSCONDED = "ABSCONDED", "Absconded"

        OTHER = "OTHER", "Other"

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