# Generated by Django 3.1.2 on 2020-11-14 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('role', models.CharField(choices=[('admin', 'admin'), ('medical_staff', 'medical staff'), ('patient', 'patient')], max_length=20)),
            ],
            options={
                'db_table': 'login_info',
            },
        ),
    ]