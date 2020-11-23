from rest_framework import serializers
from .models import Account, Patient, Doctor

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        # fields = ['name', 'age', 'phoneNumber', 'allergies', 'bloodType']
        fields = '__all__'


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        # fields = ['name', 'age', 'phoneNumber']
        fields = '__all__'

class AccountSerializer(serializers.ModelSerializer):
    # patient = PatientSerializer()
    # doctor = DoctorSerializer()
    class Meta:
        model = Account
        # fields = ['id','username', 'password','role','personal_info']
        fields = '__all__'
    # def create(self, validated_data): # only patient can create account
    #     patient = validated_data.pop('patient')
    #     account = Account.objects.create(**validated_data)
    #     Patient.objects.create(account=account, **patient)
    #     return account
