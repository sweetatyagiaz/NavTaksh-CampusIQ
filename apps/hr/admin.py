from django.contrib import admin

from .models import Department, Designation, Employment, Resignation, TeacherSubject


admin.site.register([Department, Designation, Employment, Resignation, 
                     TeacherSubject])