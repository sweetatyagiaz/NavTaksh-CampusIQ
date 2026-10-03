from django.db import models

# Create your models here.

class Exam(models.Model):

    school = models.ForeignKey(
        "organizations.School",
        on_delete=models.CASCADE
    )

    name = models.CharField(
        max_length=100
    )

    start_date = models.DateField()

    end_date = models.DateField()

    def __str__(self):
        return self.name

class Mark(models.Model):

    exam = models.ForeignKey(
        Exam,
        on_delete=models.CASCADE
    )

    student = models.ForeignKey(
        "students.Student",
        on_delete=models.CASCADE
    )

    subject = models.ForeignKey(
        "academics.Subject",
        on_delete=models.CASCADE
    )

    marks_obtained = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )

    max_marks = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )

    class Meta:

        unique_together = (
            "exam",
            "student",
            "subject"
        )

