from rest_framework import serializers
from .models import Account, PersonalInfo, MedicalInfo, DepartmentInfo

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


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

