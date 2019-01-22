from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class CustomUser(AbstractUser):
    # add additional fields in here
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    mobile = models.CharField(max_length=50)
    postcode = models.CharField(max_length=20, null=False)
    door_number = models.IntegerField(default=1, null=False)
    postcode_ref = models.OneToOneField('scheduleapi.PostcodeTBL', on_delete=models.CASCADE, null=True)
    # token = models.CharField(default=uuid.uuid4())

    def __str__(self):
        return self.email

