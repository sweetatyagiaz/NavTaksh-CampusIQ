from django.db import models

from apps.core.models import BaseModel
from apps.core.constants import Gender


# class Resignation(BaseModel):
#     """
#     Employee resignation / separation record.
#     """

#     class ReasonType(models.TextChoices):

#         RESIGNED = "RESIGNED", "Resigned"

#         RETIRED = "RETIRED", "Retired"

#         TERMINATED = "TERMINATED", "Terminated"

#         CONTRACT_ENDED = "CONTRACT_ENDED", "Contract Ended"

#         TRANSFERRED = "TRANSFERRED", "Transferred"

#         DECEASED = "DECEASED", "Deceased"

#         ABSCONDED = "ABSCONDED", "Absconded"

#         OTHER = "OTHER", "Other"

#     employment = models.OneToOneField(
#         "hr.Employment",
#         on_delete=models.CASCADE,
#         related_name="resignation"
#     )

#     reason_type = models.CharField(
#         max_length=30,
#         choices=ReasonType.choices
#     )

#     resignation_date = models.DateField(
#         help_text="Last working day"
#     )

#     reason_details = models.TextField(
#         blank=True,
#         help_text="Detailed explanation"
#     )

#     relieving_letter = models.FileField(
#         upload_to="hr/resignations/",
#         blank=True,
#         null=True
#     )

#     exit_interview_notes = models.TextField(
#         blank=True
#     )

#     is_rehire_eligible = models.BooleanField(
#         default=True
#     )

#     class Meta:
#         db_table = "resignation"
#         ordering = ["-resignation_date"]

#     def get_slug_source(self):
#         return (
#             f"{self.employment.employee_code}-"
#             f"{self.reason_type}"
#         )

#     def __str__(self):
#         return (
#             f"{self.employment.employee_code} - "
#             f"{self.reason_type}"
#         )