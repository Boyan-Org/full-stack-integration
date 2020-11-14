from django.db import models
from rest_framework import serializers


class Message(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('url', 'subject', 'body', 'pk')


class Login_Info(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    role = models.CharField(
        max_length=20,
        choices=(
            ('admin', 'admin'),
            ('medical_staff', 'medical staff'),
            ('patient', 'patient'),
        )
    )

    class Meta:
        db_table = 'login_info'
