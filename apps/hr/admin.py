from django.contrib import admin

from .models import Person, Department, Designation, Employment, Resignation


admin.site.register([Person, Department, Designation, Employment, Resignation])