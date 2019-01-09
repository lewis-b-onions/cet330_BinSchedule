from django.db import models


# Create your models here.


class CouncilRegistration(models.Model):
    council_id = models.AutoField(primary_key=True)
    council_name = models.CharField(max_length=60)
    council_code = models.CharField(max_length=60)
    council_address = models.CharField(max_length=60)

    def __str__(self):
        return self.council_name


class BinType(models.Model):
    bin_id = models.AutoField(primary_key=True)
    bin_type = models.CharField(max_length=60)

    def __str__(self):
        #  return 'Bin Id = {0} & Bin type = {1}'.format(self.bin_id, self.bin_type)
        return self.bin_type


class BinSchedule(models.Model):
    schedule_id = models.AutoField(primary_key=True)
    council_id = models.ForeignKey('CouncilRegistration', on_delete=models.CASCADE, null=True)
    date = models.DateField(null=False, blank=False)
    bin_id = models.ForeignKey('BinType', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return 'Bin Schedule {0}'.format(self.schedule_id)