from django.db import models

# Create your models here.

class AcademicYear(models.Model):

    school = models.ForeignKey(
        "organizations.School",
        on_delete=models.CASCADE
    )

    name = models.CharField(
        max_length=100
    )

    start_date = models.DateField()

    end_date = models.DateField()

    is_current = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.name

class ClassRoom(models.Model):

    school = models.ForeignKey(
        "organizations.School",
        on_delete=models.CASCADE
    )

    academic_year = models.ForeignKey(
        AcademicYear,
        on_delete=models.CASCADE
    )

    name = models.CharField(
        max_length=50
    )

    def __str__(self):
        return self.name

class Section(models.Model):

    classroom = models.ForeignKey(
        ClassRoom,
        on_delete=models.CASCADE
    )

    name = models.CharField(
        max_length=10
    )

    def __str__(self):
        return f"{self.classroom} - {self.name}"

class Subject(models.Model):

    school = models.ForeignKey(
        "organizations.School",
        on_delete=models.CASCADE
    )

    code = models.CharField(
        max_length=20
    )

    name = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.name
    