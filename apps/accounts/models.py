from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.core.models import BaseModel

class Role(models.Model):

    class RoleType(models.TextChoices):
        PLATFORM = "PLATFORM", "Platform"
        INSTITUTION = "INSTITUTION", "Institution"

    code = models.CharField(
        max_length=50,
        unique=True
    )

    name = models.CharField(
        max_length=100
    )

    role_type = models.CharField(
        max_length=20,
        choices=RoleType.choices,
        default=RoleType.INSTITUTION
    )

    description = models.TextField(
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        db_table = "role"
        ordering = ["role_type", "name"]

    def __str__(self):
        return self.name

class User(AbstractUser):

    school = models.ForeignKey(
        "organizations.School",
        on_delete=models.PROTECT,
        related_name="users",
        null=True,
        blank=True
    )

    mobile = models.CharField(
        max_length=20,
        blank=True
    )

    is_platform_admin = models.BooleanField(
        default=False
    )

    def has_role(self, role_code):

        return self.roles.filter(
            role__code=role_code
        ).exists()

    class Meta:
        db_table = "user"


class UserRole(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="roles"
    )

    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
        related_name="users"
    )

    assigned_at = models.DateTimeField(
        auto_now_add=True
    )

    assigned_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_roles"
    )

    is_active = models.BooleanField(
        default=True
    )

    class Meta:
        db_table = "user_role"

        unique_together = (
            "user",
            "role"
        )

        ordering = [
            "user",
            "role"
        ]

    def __str__(self):
        return f"{self.user.username} - {self.role.name}"

class Permission(models.Model):

    code = models.CharField(
        max_length=100,
        unique=True
    )

    name = models.CharField(
        max_length=255
    )

    module = models.CharField(
        max_length=100
    )

    description = models.TextField(
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    class Meta:
        db_table = "permission"
        ordering = [
            "module",
            "name"
        ]

    def __str__(self):
        return self.name

class RolePermission(models.Model):

    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
        related_name="permissions"
    )

    permission = models.ForeignKey(
        Permission,
        on_delete=models.CASCADE,
        related_name="roles"
    )

    class Meta:
        db_table = "role_permission"

        unique_together = (
            "role",
            "permission"
        )

    def __str__(self):
        return f"{self.role.name} - {self.permission.name}"







