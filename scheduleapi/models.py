from django.db import models

# Create your models here.

class CouncilRegistration (models.Model):
    council_id = models.AutoField(primary_key=True)
    council_name = models.CharField(max_length=60)
    council_code = models.CharField(max_length=60)
    council_address = models.CharField(max_length=60)


class BinSchedule (models.Model):
    schedule_id = models.AutoField(primary_key=True)
    council_id = models.ForeignKey('CouncilRegistration', on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(null=False, blank=False)
    bin_type = models.CharField(max_length=60)


