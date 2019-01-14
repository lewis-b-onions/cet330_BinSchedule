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
    date = models.DateTimeField(null=False, blank=False)
    bin_id = models.ForeignKey('BinType', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return 'Bin Schedule {0}'.format(self.schedule_id)


class PostcodeTBL (models.Model):
    postcode_id = models.AutoField(primary_key=True)
    postcode = models.CharField(max_length=10)
    council_id = models.ForeignKey('CouncilRegistration', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.postcode


class PostcodeGrouping (models.Model):
    grouping_id = models.AutoField(primary_key=True)
    # New Int grouping ID to group the postcodes
    group_id = models.IntegerField(null=False)
    postcode_id = models.ForeignKey('PostcodeTBL', on_delete=models.CASCADE, null=True)
    area = models.CharField(max_length=60)


class BinScheduleMapping (models.Model):
    id = models.AutoField(primary_key=True)
    binschedule_id = models.OneToOneField('BinSchedule', on_delete=models.CASCADE, null=True)
    postcodegrouping_id = models.OneToOneField('PostcodeGrouping', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return 'Bin Schedule Mapping: {0}'.format(self.binschedule_id)


class UserBinMap (models.Model):
    id = models.AutoField(primary_key=True)
    userbin_id = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, null=True)
    bin_id = models.ForeignKey('BinType', on_delete=models.CASCADE, null=True)