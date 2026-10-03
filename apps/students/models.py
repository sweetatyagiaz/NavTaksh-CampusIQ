from django.db import models


class Parent(models.Model):

    school = models.ForeignKey(
        "organizations.School",
        on_delete=models.CASCADE
    )

    father_name = models.CharField(
        max_length=255,
        blank=True
    )

    mother_name = models.CharField(
        max_length=255,
        blank=True
    )

    mobile = models.CharField(
        max_length=20
    )

    email = models.EmailField(
        blank=True
    )

    address = models.TextField(
        blank=True
    )

    def __str__(self):
        return self.mobile

class StudentStatus(models.TextChoices):

    ACTIVE = "ACTIVE", "Active"
    PROMOTED = "PROMOTED", "Promoted"
    TRANSFERRED = "TRANSFERRED", "Transferred"
    ALUMNI = "ALUMNI", "Alumni"
    DROPPED = "DROPPED", "Dropped"

class Student(models.Model):

    school = models.ForeignKey(
        "organizations.School",
        on_delete=models.CASCADE
    )

    admission_no = models.CharField(
        max_length=50,
        unique=True
    )

    first_name = models.CharField(
        max_length=100
    )

    last_name = models.CharField(
        max_length=100,
        blank=True
    )

    gender = models.CharField(
        max_length=10
    )

    dob = models.DateField()

    classroom = models.ForeignKey(
        "academics.ClassRoom",
        on_delete=models.PROTECT
    )

    section = models.ForeignKey(
        "academics.Section",
        on_delete=models.PROTECT
    )

    parent = models.ForeignKey(
        Parent,
        on_delete=models.SET_NULL,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=StudentStatus.choices,
        default=StudentStatus.ACTIVE
    )

    admission_date = models.DateField()

    photo = models.ImageField(
        upload_to="students/photos/",
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.admission_no} - {self.first_name}"

class StudentDocument(models.Model):

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="documents"
    )

    name = models.CharField(
        max_length=100
    )

    file = models.FileField(
        upload_to="students/documents/"
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

