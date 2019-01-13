from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # add additional fields in here
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    mobile = models.CharField(max_length=50)
    postcode = models.CharField(max_length=20, null=False)
    door_number = models.IntegerField(default=0, null=False)

    def __str__(self):
        return self.email