from django.db import models
from django.conf import settings
from django.db.models.fields import related


class Account(models.Model):
    username = models.CharField(max_length=20, unique=True,blank=False)
    password = models.CharField(max_length=20, blank=False)
    role = models.CharField(
        max_length=20,
        blank=False,
        choices=(
            ('admin', 'admin'),
            ('staff', 'staff'),
            ('patient', 'patient'),
            ('doctor', 'doctor'),
        )
    )
    class Meta:
        db_table = 'account'

class PersonalInfo(models.Model):
    id = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
        primary_key=True,
        db_column='id',
    )
    name = models.CharField(max_length=100, blank=False)
    gender = models.CharField(max_length=100)
    dateOfBirth = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=11)
    address = models.CharField(max_length=100)
    maritalStatus = models.CharField(max_length=100)



    class Meta:
        db_table = 'personal_info'


class MedicalInfo(models.Model):
    id = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
        primary_key=True,
        db_column='id',
    )
    height = models.IntegerField()
    weight = models.IntegerField()
    familyHistory = models.CharField(max_length=100)
    surgicalHistory = models.CharField(max_length=100)
    allergies = models.CharField(max_length=100)
    bloodType = models.CharField(max_length=1)
    habits = models.CharField(max_length=100)
    class Meta:
        db_table = 'medical_info'

class DepartmentInfo(models.Model):
    id = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
        primary_key=True,
        db_column='id',
    )
    department = models.CharField(max_length=100)
    supervisor = models.CharField(max_length=100)
    class Meta:
        db_table = 'dept_info'

class MedicalRecord(models.Model):
    recordID = models.IntegerField(primary_key=True)
    patientID = models.ForeignKey(Account, on_delete=models.CASCADE, blank=False, related_name='+', db_column='patientID')
    doctorID = models.ForeignKey(Account, on_delete=models.CASCADE, blank=False, related_name='+', db_column='doctorID')
    date = models.DateTimeField(blank=False)
    symptoms = models.CharField(max_length=300)
    treatments = models.CharField(max_length=300)
    diagnosis = models.CharField(max_length=300)
    attachmentNb = models.IntegerField(default=0)

    class Meta:
        db_table = 'medical_record'

class WorkingHour(models.Model):
    id = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
        primary_key=True,
        db_column='id',
    )
    monM = models.BooleanField(default=False)
    monA = models.BooleanField(default=False)
    tueM = models.BooleanField(default=False)
    tueA = models.BooleanField(default=False)
    wedM = models.BooleanField(default=False)
    wedA = models.BooleanField(default=False)
    thrM = models.BooleanField(default=False)
    thrA = models.BooleanField(default=False)
    friM = models.BooleanField(default=False)
    friA = models.BooleanField(default=False)

    class Meta:
        db_table = 'working_hour'

class Appointment(models.Model):
    appointmentID = models.IntegerField(primary_key=True)
    patientID = models.ForeignKey(Account, on_delete=models.CASCADE, blank=False, related_name='+', db_column='patientID')
    doctorID = models.ForeignKey(Account, on_delete=models.CASCADE, blank=False, related_name='+', db_column='doctorID')
    dateTime = models.DateTimeField(blank=False)

    class Meta:
        db_table = 'appointment'
