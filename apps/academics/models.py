from django.db import models

from apps.core.models import BaseModel

class AcademicYear(models.Model):

    school = models.ForeignKey(
        "organizations.School",
        on_delete=models.CASCADE,
        related_name="academic_years"
    )

    code = models.CharField(
        max_length=20
    )

    name = models.CharField(
        max_length=100
    )

    start_date = models.DateField()

    end_date = models.DateField()

    is_current = models.BooleanField(
        default=False
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        db_table = "academic_year"

        unique_together = (
            "school",
            "code"
        )

        ordering = [
            "-start_date"
        ]

    def __str__(self):
        return f"{self.school.name} - {self.name}"


class Class(models.Model):

    school = models.ForeignKey(
        "organizations.School",
        on_delete=models.CASCADE,
        related_name="classes"
    )

    academic_year = models.ForeignKey(
        "academics.AcademicYear",
        on_delete=models.CASCADE,
        related_name="classes"
    )

    code = models.CharField(
        max_length=20
    )

    name = models.CharField(
        max_length=100
    )

    description = models.TextField(
        blank=True
    )

    display_order = models.PositiveIntegerField(
        default=1
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        db_table = "class"

        unique_together = (
            "school",
            "academic_year",
            "code"
        )

        ordering = [
            "display_order",
            "name"
        ]

    def __str__(self):
        return self.name


class Section(models.Model):

    school = models.ForeignKey(
        "organizations.School",
        on_delete=models.CASCADE
    )

    academic_year = models.ForeignKey(
        "academics.AcademicYear",
        on_delete=models.CASCADE
    )

    classroom = models.ForeignKey(
        "academics.Class",
        on_delete=models.CASCADE,
        related_name="sections"
    )

    code = models.CharField(
        max_length=20
    )

    name = models.CharField(
        max_length=50
    )

    capacity = models.PositiveIntegerField(
        default=50
    )

    is_active = models.BooleanField(
        default=True
    )

    class Meta:

        db_table = "section"

        unique_together = (
            "classroom",
            "code"
        )

    def __str__(self):
        return f"{self.classroom.name} - {self.name}"


class Subject(models.Model):

    school = models.ForeignKey(
        "organizations.School",
        on_delete=models.CASCADE,
        related_name="subjects"
    )

    code = models.CharField(
        max_length=20
    )

    name = models.CharField(
        max_length=255
    )

    description = models.TextField(
        blank=True
    )

    is_optional = models.BooleanField(
        default=False
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        db_table = "subject"

        unique_together = (
            "school",
            "code"
        )

        ordering = [
            "name"
        ]

    def __str__(self):
        return self.name


class ClassSubject(models.Model):

    school = models.ForeignKey(
        "organizations.School",
        on_delete=models.CASCADE
    )

    academic_year = models.ForeignKey(
        "academics.AcademicYear",
        on_delete=models.CASCADE
    )

    classroom = models.ForeignKey(
        "academics.Class",
        on_delete=models.CASCADE,
        related_name="class_subjects"
    )

    subject = models.ForeignKey(
        "academics.Subject",
        on_delete=models.CASCADE,
        related_name="subject_classes"
    )

    is_optional = models.BooleanField(
        default=False
    )

    is_active = models.BooleanField(
        default=True
    )

    class Meta:

        db_table = "class_subject"

        unique_together = (
            "classroom",
            "subject"
        )

    def __str__(self):
        return f"{self.classroom.name} - {self.subject.name}"



class TeacherSubject(BaseModel):

    employee = models.ForeignKey(
        "hr.Employee",
        on_delete=models.CASCADE,
        related_name="teacher_subjects"
    )

    subject = models.ForeignKey(
        "academics.Subject",
        on_delete=models.PROTECT,
        related_name="teacher_subjects"
    )

    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=5.0
    )

    remarks = models.TextField(
        blank=True
    )

    class Meta:
        db_table = "teacher_subject"

        unique_together = (
            "employee",
            "subject"
        )

        ordering = [
            "employee",
            "subject"
        ]

    def get_slug_source(self):
        return (
            f"{self.employee}-"
            f"{self.subject}"
        )

    def __str__(self):
        return (
            f"{self.employee} - "
            f"{self.subject}"
        )


class ClassSection(BaseModel):

    academic_year = models.ForeignKey(
        "academics.AcademicYear",
        on_delete=models.PROTECT,
        related_name="class_sections"
    )

    classroom = models.ForeignKey(
        "academics.Class",
        on_delete=models.PROTECT,
        related_name="class_sections"
    )

    section = models.ForeignKey(
        "academics.Section",
        on_delete=models.PROTECT,
        related_name="class_sections"
    )

    capacity = models.PositiveIntegerField(
        default=40
    )

    class Meta:

        db_table = "class_section"

        unique_together = (
            "academic_year",
            "classroom",
            "section"
        )

        ordering = [
            "academic_year",
            "classroom",
            "section"
        ]

    def get_slug_source(self):
        return (
            f"{self.academic_year}-"
            f"{self.classroom}-"
            f"{self.section}"
        )

    def __str__(self):
        return (
            f"{self.classroom} - "
            f"{self.section}"
        )

class TeacherClass(BaseModel):

    employee = models.ForeignKey(
        "hr.Employee",
        on_delete=models.CASCADE,
        related_name="teacher_classes"
    )

    class_section = models.ForeignKey(
        "academics.ClassSection",
        on_delete=models.CASCADE,
        related_name="teacher_classes"
    )

    subject = models.ForeignKey(
        "academics.Subject",
        on_delete=models.PROTECT,
        related_name="teacher_classes"
    )

    class Meta:

        db_table = "teacher_class"

        unique_together = (
            "employee",
            "class_section",
            "subject"
        )

    def get_slug_source(self):
        return (
            f"{self.employee}-"
            f"{self.class_section}-"
            f"{self.subject}"
        )


class ClassTeacher(BaseModel):

    class_section = models.OneToOneField(
        "academics.ClassSection",
        on_delete=models.CASCADE,
        related_name="class_teacher"
    )

    employee = models.ForeignKey(
        "hr.Employee",
        on_delete=models.PROTECT,
        related_name="class_teacher_assignments"
    )

    class Meta:

        db_table = "class_teacher"

    def get_slug_source(self):
        return (
            f"{self.class_section}"
        )


