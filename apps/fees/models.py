from django.db import models

# Create your models here.

class FeeCategory(models.Model):

    school = models.ForeignKey(
        "organizations.School",
        on_delete=models.CASCADE
    )

    name = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.name

class FeeStructure(models.Model):

    school = models.ForeignKey(
        "organizations.School",
        on_delete=models.CASCADE
    )

    classroom = models.ForeignKey(
        "academics.ClassRoom",
        on_delete=models.CASCADE
    )

    fee_category = models.ForeignKey(
        FeeCategory,
        on_delete=models.CASCADE
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

class FeeStatus(models.TextChoices):

    PENDING = "PENDING", "Pending"
    PARTIAL = "PARTIAL", "Partial"
    PAID = "PAID", "Paid"
    OVERDUE = "OVERDUE", "Overdue"

class StudentFee(models.Model):

    student = models.ForeignKey(
        "students.Student",
        on_delete=models.CASCADE
    )

    fee_structure = models.ForeignKey(
        FeeStructure,
        on_delete=models.CASCADE
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    paid_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    due_date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=FeeStatus.choices,
        default=FeeStatus.PENDING
    )

