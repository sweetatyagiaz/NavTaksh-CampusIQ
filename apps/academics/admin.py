from django.contrib import admin

from .models import AcademicYear, Class, Subject, ClassSubject

# admin.site.register([Subject])


@admin.register(AcademicYear)
class AcademicYearAdmin(admin.ModelAdmin):

    list_display = (
        "school",
        "code",
        "name",
        "start_date",
        "end_date",
        "is_current",
        "is_active"
    )

    list_filter = (
        "school",
        "is_current",
        "is_active"
    )

    search_fields = (
        "code",
        "name"
    )

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):

    list_display = (
        "school",
        "academic_year",
        "code",
        "name",
        "display_order",
        "is_active"
    )

    list_filter = (
        "school",
        "academic_year",
        "is_active"
    )

    search_fields = (
        "code",
        "name"
    )


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):

    list_display = (
        "code",
        "name",
        "is_optional",
        "is_active"
    )

    search_fields = (
        "code",
        "name"
    )


@admin.register(ClassSubject)
class ClassSubjectAdmin(admin.ModelAdmin):

    list_display = (
        "classroom",
        "subject",
        "is_optional"
    )

    list_filter = (
        "classroom",
    )


