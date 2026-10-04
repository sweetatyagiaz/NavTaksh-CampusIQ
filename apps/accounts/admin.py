from django.contrib import admin

from .models import Role, User, UserRole, Permission, RolePermission


admin.site.register([Role, User])


@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "role",
        "is_active",
        "assigned_at"
    )

    list_filter = (
        "role",
        "is_active"
    )

    search_fields = (
        "user__username",
        "role__name"
    )

@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):

    list_display = (
        "code",
        "name",
        "module",
        "is_active"
    )

    list_filter = (
        "module",
        "is_active"
    )

    search_fields = (
        "code",
        "name"
    )


@admin.register(RolePermission)
class RolePermissionAdmin(admin.ModelAdmin):

    list_display = (
        "role",
        "permission"
    )

    list_filter = (
        "role",
    )