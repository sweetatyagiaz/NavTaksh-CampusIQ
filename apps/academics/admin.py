from django.contrib import admin

from .models import AcademicYear, Subject, TeacherSubject

admin.site.register([AcademicYear, Subject, TeacherSubject])
