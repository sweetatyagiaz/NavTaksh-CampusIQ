from django.db import models

# Create your models here.
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




