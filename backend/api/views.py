from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework import viewsets

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from .models import Account, PersonalInfo, MedicalInfo, DepartmentInfo
from .serializers import AccountSerializer, PISerializer, DISerializer, MISerializer
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
            role    : "patient", ..} (including all the personal_info)

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
            id = account.id
            data.update({"id": id})
            personal_info = PersonalInfo.objects.get(id=id)
            data.update({"name",personal_info.name})
            return Response(data=data, status=HTTP_200_OK)


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
            name    : "Boyan Xu"
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
    name = data['name']
    serializer = AccountSerializer(data=data)
    if serializer.is_valid():
        account = serializer.save()
        personal_info = PersonalInfo(name=name, id=account)
        personal_info.save()
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.data, status=status.HTTP_409_CONFLICT)


class PIViewSet(viewsets.ModelViewSet):
    """
    provides `list`, `create`, `retrieve`, `update` and `destroy` actions
    """
    queryset = PersonalInfo.objects.all()
    serializer_class = PISerializer


class MIViewSet(viewsets.ModelViewSet):
    """
    provides `list`, `create`, `retrieve`, `update` and `destroy` actions
    """
    queryset = MedicalInfo.objects.all()
    serializer_class = MISerializer

class DIViewSet(viewsets.ModelViewSet):
    """
    provides `list`, `create`, `retrieve`, `update` and `destroy` actions
    """
    queryset = DepartmentInfo.objects.all()
    serializer_class = DISerializer
