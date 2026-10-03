from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.organizations.models import School

# Create your models here.


class User(AbstractUser):

    school = models.ForeignKey(
        "organizations.School",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="users"
    )

    mobile = models.CharField(
        max_length=20,
        blank=True
    )