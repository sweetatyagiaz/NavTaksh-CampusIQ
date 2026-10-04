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

class PersonIdentity(BaseModel):

    class IdentityType(models.IntegerChoices):

        AADHAAR = 1, "Aadhaar"

        PAN = 2, "PAN"

        PASSPORT = 3, "Passport"

        DRIVING_LICENSE = 4, "Driving License"

        VOTER_ID = 5, "Voter ID"

        BIRTH_CERTIFICATE = 6, "Birth Certificate"

        OTHER = 99, "Other"

    person = models.ForeignKey(
        "people.Person",
        on_delete=models.CASCADE,
        related_name="identities"
    )

    identity_type = models.PositiveSmallIntegerField(
        choices=IdentityType.choices,
        db_index=True
    )

    identity_number = models.CharField(
        max_length=100,
        db_index=True
    )

    issue_date = models.DateField(
        null=True,
        blank=True
    )

    expiry_date = models.DateField(
        null=True,
        blank=True
    )

    is_verified = models.BooleanField(
        default=False
    )

    remarks = models.TextField(
        blank=True
    )

    class Meta:
        db_table = "person_identity"

        ordering = [
            "person",
            "identity_type"
        ]

        constraints = [
            models.UniqueConstraint(
                fields=[
                    "identity_type",
                    "identity_number"
                ],
                name="uq_identity_type_number"
            )
        ]

    def get_slug_source(self):
        return (
            f"{self.person_id}-"
            f"{self.identity_type}-"
            f"{self.identity_number}"
        )

    def __str__(self):
        return (
            f"{self.get_identity_type_display()} - "
            f"{self.identity_number}"
        )


class PersonContact(BaseModel):

    class ContactType(models.IntegerChoices):

        MOBILE = 1, "Mobile"

        EMAIL = 2, "Email"

        WHATSAPP = 3, "WhatsApp"

        ALTERNATE_MOBILE = 4, "Alternate Mobile"

        LANDLINE = 5, "Landline"

        EMERGENCY = 6, "Emergency Contact"

        OTHER = 99, "Other"

    person = models.ForeignKey(
        "people.Person",
        on_delete=models.CASCADE,
        related_name="contacts"
    )

    contact_type = models.PositiveSmallIntegerField(
        choices=ContactType.choices,
        db_index=True
    )

    value = models.CharField(
        max_length=255,
        db_index=True
    )

    is_primary = models.BooleanField(
        default=False
    )

    is_verified = models.BooleanField(
        default=False
    )

    remarks = models.TextField(
        blank=True
    )

    class Meta:
        db_table = "person_contact"

        ordering = [
            "person",
            "contact_type"
        ]

        constraints = [
            models.UniqueConstraint(
                fields=[
                    "contact_type",
                    "value"
                ],
                name="uq_contact_type_value"
            )
        ]

    def get_slug_source(self):
        return (
            f"{self.person_id}-"
            f"{self.contact_type}-"
            f"{self.value}"
        )

    def __str__(self):
        return (
            f"{self.get_contact_type_display()} - "
            f"{self.value}"
        )


class PersonAddress(BaseModel):

    class AddressType(models.IntegerChoices):

        HOME = 1, "Home"

        PERMANENT = 2, "Permanent"

        CORRESPONDENCE = 3, "Correspondence"

        OFFICE = 4, "Office"

        HOSTEL = 5, "Hostel"

        OTHER = 99, "Other"

    person = models.ForeignKey(
        "people.Person",
        on_delete=models.CASCADE,
        related_name="addresses"
    )

    address_type = models.PositiveSmallIntegerField(
        choices=AddressType.choices,
        default=AddressType.HOME,
        db_index=True
    )

    address_line_1 = models.CharField(
        max_length=255
    )

    address_line_2 = models.CharField(
        max_length=255,
        blank=True
    )

    landmark = models.CharField(
        max_length=255,
        blank=True
    )

    city = models.CharField(
        max_length=100
    )

    district = models.CharField(
        max_length=100,
        blank=True
    )

    state = models.CharField(
        max_length=100
    )

    country = models.CharField(
        max_length=100,
        default="India"
    )

    postal_code = models.CharField(
        max_length=20
    )

    latitude = models.DecimalField(
        max_digits=10,
        decimal_places=7,
        null=True,
        blank=True
    )

    longitude = models.DecimalField(
        max_digits=10,
        decimal_places=7,
        null=True,
        blank=True
    )

    is_primary = models.BooleanField(
        default=False
    )

    remarks = models.TextField(
        blank=True
    )

    class Meta:
        db_table = "person_address"

        ordering = [
            "person",
            "address_type"
        ]

    def get_slug_source(self):
        return (
            f"{self.person_id}-"
            f"{self.address_type}-"
            f"{self.city}"
        )

    def __str__(self):
        return (
            f"{self.address_line_1}, "
            f"{self.city}, "
            f"{self.state}"
        )




