# Generated by Django 3.1.2 on 2020-11-25 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20201125_0822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinfo',
            name='dateOfBirth',
            field=models.CharField(max_length=100),
        ),
    ]