# Generated by Django 3.1.2 on 2020-12-09 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('role', models.CharField(choices=[('admin', 'admin'), ('staff', 'staff'), ('patient', 'patient'), ('doctor', 'doctor')], max_length=20)),
            ],
            options={
                'db_table': 'account',
            },
        ),
        migrations.CreateModel(
            name='DepartmentInfo',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.account')),
                ('department', models.CharField(blank=True, max_length=100)),
                ('supervisor', models.CharField(blank=True, max_length=100)),
                ('workingHour', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'db_table': 'dept_info',
            },
        ),
        migrations.CreateModel(
            name='MedicalInfo',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.account')),
                ('height', models.IntegerField(blank=True, default=0)),
                ('weight', models.IntegerField(blank=True, default=0)),
                ('familyHistory', models.CharField(blank=True, max_length=100)),
                ('surgicalHistory', models.CharField(blank=True, max_length=100)),
                ('allergies', models.CharField(blank=True, max_length=100)),
                ('bloodType', models.CharField(blank=True, max_length=1)),
                ('habits', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'db_table': 'medical_info',
            },
        ),
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.account')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(blank=True, max_length=100)),
                ('dateOfBirth', models.CharField(blank=True, max_length=100)),
                ('email', models.CharField(blank=True, max_length=100)),
                ('phoneNumber', models.CharField(blank=True, max_length=11)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('maritalStatus', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'db_table': 'personal_info',
            },
        ),
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('recordID', models.AutoField(primary_key=True, serialize=False)),
                ('dateTime', models.DateTimeField()),
                ('symptoms', models.CharField(blank=True, max_length=300)),
                ('treatments', models.CharField(blank=True, max_length=300)),
                ('diagnosis', models.CharField(blank=True, max_length=300)),
                ('attachmentNb', models.IntegerField(blank=True, default=0)),
                ('flag', models.BooleanField()),
                ('doctor', models.ForeignKey(db_column='doctor_id', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='api.account')),
                ('patient', models.ForeignKey(db_column='patient_id', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='api.account')),
            ],
            options={
                'db_table': 'medical_record',
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('appointmentID', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('time', models.CharField(choices=[('morning', 'morning'), ('afternoon', 'afternoon')], max_length=10)),
                ('submitTime', models.DateTimeField()),
                ('doctor', models.ForeignKey(db_column='doctor_id', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='api.account')),
                ('patient', models.ForeignKey(db_column='patient_id', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='api.account')),
            ],
            options={
                'db_table': 'appointment',
            },
        ),
    ]
