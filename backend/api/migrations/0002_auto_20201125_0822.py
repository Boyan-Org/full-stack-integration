# Generated by Django 3.1.2 on 2020-11-25 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinfo',
            name='dateOfBirth',
            field=models.DateField(blank=True),
        ),
    ]
