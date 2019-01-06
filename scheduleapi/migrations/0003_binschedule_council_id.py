# Generated by Django 2.1.4 on 2019-01-04 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheduleapi', '0002_remove_binschedule_council_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='binschedule',
            name='council_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='scheduleapi.CouncilRegistration'),
            preserve_default=False,
        ),
    ]
