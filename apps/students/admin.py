from django.contrib import admin
from .models import Student, StudentParent


admin.site.register([Student, StudentParent])