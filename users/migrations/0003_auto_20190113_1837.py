# Generated by Django 2.0.7 on 2019-01-13 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190113_1720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='user_id',
        ),
        migrations.AddField(
            model_name='customuser',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
