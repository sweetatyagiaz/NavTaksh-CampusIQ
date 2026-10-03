from django.contrib import admin
from .models import Parent, Student, StudentDocument


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = (
        "admission_no",
        "first_name",
        "last_name",
        "classroom",
        "section",
        "status",
    )

    search_fields = (
        "admission_no",
        "first_name",
        "last_name",
    )

    list_filter = (
        "status",
        "classroom",
        "section",
    )


admin.site.register(Parent)
admin.site.register(StudentDocument)