from django.db import models
from django.conf import settings


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
        primary_key=True
    )
    name = models.CharField(max_length=100, blank=False)
    gender = models.CharField(max_length=100)
    dateOfBirth = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=11)
    address = models.CharField(max_length=100)

    class Meta:
        db_table = 'personal_info'


class MedicalInfo(models.Model):
    id = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
        primary_key=True
    )
    height = models.IntegerField()
    weight = models.IntegerField()
    familyHistory = models.CharField(max_length=100)
    surgicalHistory = models.CharField(max_length=100)
    allergies = models.CharField(max_length=100)
    bloodType = models.CharField(max_length=1)
    class Meta:
        db_table = 'medical_info'

class DepartmentInfo(models.Model):
    id = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
        primary_key=True
    )
    department = models.CharField(max_length=100)
    supervisor = models.CharField(max_length=100)
    class Meta:
        db_table = 'department_info'