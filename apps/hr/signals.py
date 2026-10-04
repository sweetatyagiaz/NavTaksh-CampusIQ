from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Employee
from .models import EmployeeResignation


@receiver(
    post_save,
    sender=EmployeeResignation
)
def update_employee_status(
    sender,
    instance,
    created,
    **kwargs
):

    if not created:
        return

    employee = instance.employee

    mapping = {
        EmployeeResignation.Reason.RESIGNED:
            Employee.Status.RESIGNED,

        EmployeeResignation.Reason.RETIRED:
            Employee.Status.RETIRED,

        EmployeeResignation.Reason.TERMINATED:
            Employee.Status.TERMINATED,

        EmployeeResignation.Reason.CONTRACT_ENDED:
            Employee.Status.TERMINATED,

        EmployeeResignation.Reason.DECEASED:
            Employee.Status.TERMINATED,

        EmployeeResignation.Reason.TRANSFERRED:
            Employee.Status.RESIGNED,
    }

    employee.status = mapping.get(
        instance.reason,
        Employee.Status.RESIGNED
    )

    employee.save(
        update_fields=["status"]
    )