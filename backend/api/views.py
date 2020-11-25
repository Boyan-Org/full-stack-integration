from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework import viewsets

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Account, Patient, Doctor
from .serializers import AccountSerializer, PatientSerializer, DoctorSerializer
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))


@api_view(['POST'])
def login(request):
    """
    PATH:
        `localhost:8000/api/login/`

    Description:
            Login request handler.

    Request Format: (JSON)

        { username: "frank",
            password: "frank" }

    Response Status:

        200: Success
        401: `password` doesn't match the `username`
        404: `username` not found

    Response Format: (JSON)

        { id: 1,
            username: "frank",
            password: "frank",
            role    : "patient", ..}

    """
    data = JSONParser().parse(request)
    try:
        account = Account.objects.get(username=data['username'])
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        if account.password != data['password']:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            role = account.role
            id = account.id
            if role == 'patient':
                # TODO: try before get
                patient = Patient.objects.get(id=id)
                serializer = PatientSerializer(patient)
                return_data = dict(serializer.data)
                return_data["role"] = role
                return_data.update(data)
                return Response(return_data, status=status.HTTP_200_OK)
            elif role == 'doctor':
                # TODO: try before get
                doctor = Doctor.objects.get(id=id)
                serializer = DoctorSerializer(doctor)
                return_data = dict(serializer.data)
                return_data["role"] = role
                return_data.update(data)
                return Response(return_data, status=status.HTTP_200_OK)
            else:
                # reserved for admin
                pass


@api_view(['POST'])
def register(request):
    """
    PATH:
        `localhost:8000/api/register/`

    Description:
        Register request handler.

    Request Format: (JSON)

        { username   : "boyan",
            password: "boyan",
            role    : "patient",
            patient : {
                name       : "Boyan Xu",
                age        : 21,
                bloodType  : "A",
                allergies  : null
                phoneNumber: 123
            }
        }

    Response Status:

        201: Success
        409: `Username` already taken by someone else

    Response Format: (JSON)

        { username: "frank",
            password: "frank",
            role    : "patient", ..
        }

    """
    data = JSONParser().parse(request)
    personal_info = data.pop('personal_info')
    serializer = AccountSerializer(data=data)
    if serializer.is_valid():
        account = serializer.save()
        if data['role'] == "patient":
            actor = Patient.objects.create(**personal_info, id=account)
        else:
            actor = Doctor.objects.create(**personal_info, id=account)
        actor.save()
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.data, status=status.HTTP_409_CONFLICT)


class PatientViewSet(viewsets.ModelViewSet):
    """
    provides `list`, `create`, `retrieve`, `update` and `destroy` actions
    """
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    """
    provides `list`, `create`, `retrieve`, `update` and `destroy` actions
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
