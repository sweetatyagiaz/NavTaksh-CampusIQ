from django.contrib import admin

from .models import Person, PersonAddress, PersonContact, PersonIdentity

# Register your models here.


admin.site.register([Person, PersonAddress, PersonContact, PersonIdentity])