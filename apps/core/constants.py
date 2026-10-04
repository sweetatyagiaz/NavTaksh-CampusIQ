from django.db import models


class Gender(models.IntegerChoices):
    NOT_AVAILABLE = 0, "Not Available"
    MALE = 1, "Male"
    FEMALE = 2, "Female"


class Status(models.IntegerChoices):
    INACTIVE = 0, "Inactive"
    ACTIVE = 1, "Active"


class YesNo(models.IntegerChoices):
    NO = 0, "No"
    YES = 1, "Yes"