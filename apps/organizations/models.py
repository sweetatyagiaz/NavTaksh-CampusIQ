from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from apps.core.models import BaseModel


class WithdrawalReason(models.TextChoices):

    VOLUNTARY = "VOLUNTARY", "Voluntary Withdrawal"

    BOARD_CHANGE = "BOARD_CHANGE", "Changed Board"

    NON_COMPLIANCE = "NON_COMPLIANCE", "Non Compliance"

    MERGER = "MERGER", "School Merger"

    CLOSURE = "CLOSURE", "School Closed"

    OTHER = "OTHER", "Other"
  
class School(models.Model):
    """
    School Master

    Represents a single school/campus within CampusIQ.

    Examples:
    - NavTaksh Public School
    - Delhi International School
    - St. Xavier's School
    """

    code = models.CharField(
        max_length=20,
        unique=True,
        db_index=True,
        help_text="Unique school code"
    )

    name = models.CharField(
        max_length=255,
        db_index=True,
        help_text="Official school name"
    )

    short_name = models.CharField(
        max_length=100,
        blank=True,
        help_text="Short name used in reports"
    )

    slug = models.SlugField(
        max_length=255,
        unique=True,
        db_index=True,
        help_text="Unique URL-friendly identifier"
    )

    registration_number = models.CharField(
        max_length=100,
        blank=True,
        unique=True,
        null=True,
        help_text="School registration number"
    )

    affiliation_number = models.CharField(
        max_length=100,
        blank=True,
        unique=True,
        null=True,
        help_text="Board affiliation number"
    )

    udise_code = models.CharField(
        max_length=50,
        blank=True,
        unique=True,
        null=True,
        help_text="UDISE code"
    )

    gst_number = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        help_text="GST registration number"
    )

    website = models.URLField(
        blank=True,
        help_text="Official school website"
    )

    email = models.EmailField(
        blank=True,
        help_text="Official school email"
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
        help_text="Primary contact number"
    )

    address_line_1 = models.CharField(
        max_length=255,
        blank=True,
        help_text="Primary address"
    )

    city = models.CharField(
        max_length=100,
        blank=True,
        db_index=True
    )

    state = models.CharField(
        max_length=100,
        blank=True,
        db_index=True
    )

    country = models.CharField(
        max_length=100,
        default="India",
        db_index=True
    )

    postal_code = models.CharField(
        max_length=20,
        blank=True
    )

    latitude = models.DecimalField(
        max_digits=10,
        decimal_places=7,
        null=True,
        blank=True,
        help_text="GPS latitude"
    )

    longitude = models.DecimalField(
        max_digits=10,
        decimal_places=7,
        null=True,
        blank=True,
        help_text="GPS longitude"
    )

    logo = models.ImageField(
        upload_to="schools/logos/",
        blank=True,
        null=True
    )

    favicon = models.ImageField(
        upload_to="schools/favicons/",
        blank=True,
        null=True
    )

    primary_color = models.CharField(
        max_length=20,
        blank=True,
        help_text="Primary branding color (HEX)"
    )

    secondary_color = models.CharField(
        max_length=20,
        blank=True,
        help_text="Secondary branding color (HEX)"
    )

    academic_session_start_month = models.PositiveSmallIntegerField(
        default=4,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(12)
        ],
        help_text="Month when academic session starts (1-12)"
    )

    is_active = models.BooleanField(
        default=True,
        db_index=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "school"
        ordering = ["name"]
        verbose_name = "School"
        verbose_name_plural = "Schools"

    def __str__(self):
        return f"{self.code} - {self.name}"

    def get_slug_source(self):
        return self.name
    
class Board(models.Model):
    """
    Education Board Information

    Examples:
    CBSE
    ICSE
    IB
    IGCSE
    State Board
    NIOS
    """

    code = models.CharField(
        max_length=20,
        unique=True,
        db_index=True,
        help_text="Unique board code"
    )

    name = models.CharField(
        max_length=255,
        unique=True,
        db_index=True,
        help_text="Board name"
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    website = models.URLField(
        blank=True
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
        db_table = "board"
        ordering = ["name"]
        verbose_name = "Board"
        verbose_name_plural = "Boards"

    def __str__(self):
        return self.code + '\t:' + self.name

    def get_slug_source(self):
        return self.name

class SchoolBoardRegistration(models.Model):
    """
    Records board affiliations obtained by a school.
    """

    school = models.ForeignKey(
        "organizations.School",
        on_delete=models.CASCADE,
        related_name="board_registrations"
    )

    board = models.ForeignKey(
        "organizations.Board",
        on_delete=models.PROTECT,
        related_name="school_registrations"
    )

    registration_number = models.CharField(
        max_length=100,
        blank=True
    )

    affiliation_number = models.CharField(
        max_length=100,
        blank=True
    )

    registration_date = models.DateField()

    remarks = models.TextField(
        blank=True
    )

    is_active = models.BooleanField(
        default=True,
        db_index=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "school_board_registration"

        indexes = [
            models.Index(
                fields=["school", "board"]
            )
        ]

    def __str__(self):
        return (
            f"{self.school.name} - "
            f"{self.board.code}"
        )

class SchoolBoardWithdrawal(models.Model):
    """
    Records board affiliation withdrawal/cancellation.

    A registration remains active until a withdrawal
    record is created.
    """

    registration = models.OneToOneField(
        "organizations.SchoolBoardRegistration",
        on_delete=models.CASCADE,
        related_name="withdrawal",
        help_text="Board registration being withdrawn"
    )

    withdrawal_date = models.DateField(
        help_text="Date of withdrawal/cancellation"
    )

    reason = models.TextField(
        help_text="Reason for withdrawal"
    )

    reason_type = models.CharField(
        max_length=30,
        choices=WithdrawalReason.choices,
        default= None
    )

    supporting_document = models.FileField(
        upload_to="school_board_withdrawals/",
        blank=True,
        null=True,
        help_text="Official withdrawal/cancellation document"
    )

    remarks = models.TextField(
        blank=True,
        help_text="Additional remarks"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "school_board_withdrawal"
        ordering = ["-withdrawal_date"]
        verbose_name = "School Board Withdrawal"
        verbose_name_plural = "School Board Withdrawals"

    def __str__(self):
        return (
            f"{self.registration.school.name} | "
            f"{self.registration.board.name}"
        )