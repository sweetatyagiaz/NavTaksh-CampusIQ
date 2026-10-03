from django.contrib import admin
from .models import (
    FeeCategory,
    FeeStructure,
    StudentFee
)

admin.site.register(FeeCategory)
admin.site.register(FeeStructure)
admin.site.register(StudentFee)