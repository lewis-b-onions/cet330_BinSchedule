# Generated by Django 2.0.7 on 2019-01-20 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheduleapi', '0006_auto_20190120_1618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='binschedulemapping',
            name='binschedule_id',
        ),
        migrations.AddField(
            model_name='binschedulemapping',
            name='binschedule_id',
            field=models.ManyToManyField(to='scheduleapi.BinSchedule'),
        ),
        migrations.RemoveField(
            model_name='binschedulemapping',
            name='postcodegrouping_id',
        ),
        migrations.AddField(
            model_name='binschedulemapping',
            name='postcodegrouping_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='scheduleapi.PostcodeGrouping'),
        ),
    ]