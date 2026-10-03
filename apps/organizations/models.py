from django.db import models

# Create your models here.

from django.db import models


class School(models.Model):
    """
    Master table for educational institutions.

    This model stores the basic profile and contact information
    of a school, college, university, coaching institute,
    training center, or any educational organization managed
    within the CampusIQ ERP platform.

    All academic, administrative, financial, and operational
    modules are associated with a School record.
    """

    code = models.CharField(
        max_length=20,
        unique=True,
        help_text="Unique institution code (e.g., SCH001, DPSDELHI, IITD)"
    )

    name = models.CharField(
        max_length=255,
        help_text="Official name of the institution"
    )

    email = models.EmailField(
        blank=True,
        help_text="Primary official email address"
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
        help_text="Main contact number"
    )

    address = models.TextField(
        blank=True,
        help_text="Complete postal address"
    )

    city = models.CharField(
        max_length=100,
        blank=True,
        help_text="City where institution is located"
    )

    state = models.CharField(
        max_length=100,
        blank=True,
        help_text="State or province"
    )

    country = models.CharField(
        max_length=100,
        default="India",
        help_text="Country name"
    )

    website = models.URLField(
        blank=True
    )

    logo = models.ImageField(
        upload_to="schools/logos/",
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        default=True,
        help_text="Whether institution is currently active in the system"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        db_table = "school"
        ordering = ["name"]
        verbose_name = "School"
        verbose_name_plural = "Schools"

    def __str__(self):
        return f"{self.code} - {self.name}"