# Generated by Django 3.1.2 on 2020-11-25 10:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20201125_0826'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalinfo',
            name='habits',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='maritalStatus',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='departmentinfo',
            table='dept_info',
        ),
    ]
