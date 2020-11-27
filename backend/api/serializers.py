from rest_framework import serializers
from .models import Account, PersonalInfo, MedicalInfo, DepartmentInfo, MedicalRecord

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class PISerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInfo
        fields = '__all__'

class DISerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentInfo
        fields = '__all__'


class MISerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalInfo
        fields = '__all__'


class MRSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = '__all__'

