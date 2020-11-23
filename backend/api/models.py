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

class Patient(models.Model):
    name = models.CharField(max_length=100, blank=False)
    age = models.IntegerField(blank=False)
    phoneNumber = models.CharField(max_length=11, blank=False)
    allergies = models.CharField(max_length=100)
    bloodType = models.CharField(max_length=1, blank=False)
    account = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    class Meta:
        db_table = 'patient'

class Doctor(models.Model):
    name = models.CharField(max_length=100, blank=False)
    age = models.IntegerField(blank=False)
    phoneNumber = models.CharField(max_length=11, blank=False)
    account = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    class Meta:
        db_table = 'doctor'

