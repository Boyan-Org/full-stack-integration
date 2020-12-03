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
    gender = models.CharField(max_length=100, blank=True)
    dateOfBirth = models.CharField(max_length=100,blank=True)
    email = models.CharField(max_length=100,blank=True)
    phoneNumber = models.CharField(max_length=11,blank=True)
    address = models.CharField(max_length=100,blank=True)
    maritalStatus = models.CharField(max_length=100,blank=True)



    class Meta:
        db_table = 'personal_info'


class MedicalInfo(models.Model):
    id = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
        primary_key=True,
        db_column='id',
    )
    height = models.IntegerField(default=0, blank=True)
    weight = models.IntegerField(default=0, blank=True)
    familyHistory = models.CharField(max_length=100, blank=True)
    surgicalHistory = models.CharField(max_length=100, blank=True)
    allergies = models.CharField(max_length=100, blank=True)
    bloodType = models.CharField(max_length=1, blank=True)
    habits = models.CharField(max_length=100, blank=True)
    class Meta:
        db_table = 'medical_info'

class DepartmentInfo(models.Model):
    id = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
        primary_key=True,
        db_column='id',
    )
    department = models.CharField(max_length=100, blank=True)
    supervisor = models.CharField(max_length=100, blank=True)
    workingHour = models.CharField(max_length=100, blank=True)
    class Meta:
        db_table = 'dept_info'

class MedicalRecord(models.Model):
    recordID = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Account, on_delete=models.CASCADE, blank=False, related_name='+', db_column='patient_id')
    doctor = models.ForeignKey(Account, on_delete=models.CASCADE, blank=False, related_name='+', db_column='doctor_id')
    dateTime = models.DateTimeField(blank=False)
    symptoms = models.CharField(max_length=300, blank=True)
    treatments = models.CharField(max_length=300, blank=True)
    diagnosis = models.CharField(max_length=300, blank=True)
    attachmentNb = models.IntegerField(default=0, blank=True)
    flag = models.BooleanField(blank=False)

    class Meta:
        db_table = 'medical_record'


class Appointment(models.Model):
    appointmentID = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Account, on_delete=models.CASCADE, blank=False, related_name='+', db_column='patient_id')
    doctor = models.ForeignKey(Account, on_delete=models.CASCADE, blank=False, related_name='+', db_column='doctor_id')
    date = models.DateField(blank=False)
    time = models.CharField(
        max_length=10,
        blank=False,
        choices=(
            ('morning', 'morning'),
            ('afternoon', 'afternoon'),
        ))
    submitTime = models.DateTimeField(blank=False)


    class Meta:
        db_table = 'appointment'
