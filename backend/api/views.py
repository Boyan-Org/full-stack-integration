import json
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework import viewsets

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from .models import Account, PersonalInfo, MedicalInfo, DepartmentInfo, MedicalRecord
from .serializers import AccountSerializer, PISerializer, DISerializer, MISerializer, MRSerializer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import action
# from rest_framework.views import APIView

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
            role    : "patient"} 

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
            data.update({"name": personal_info.name})
            return Response(data=data, status=HTTP_200_OK)


@api_view(['POST'])
def register(request):
    """
    PATH:
        `localhost:8000/api/register/`

    Description:
        Register request handler.

    Request Format: (JSON)

        { username   : "userboyan",
            password: "boyan",
            role    : "patient",
            name    : "Boyan Xu"
            }
        }

    Response Status:

        201: Success
        409: `Username` already taken by someone else
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

"""
ModelViewSet

    There are two types of request headers:

        I.  Path = api/...               (Used to create/list data records)
        II. Path = api/.../<int:id>      (Used to update/delete/retrieve data records)

    I. Path = api/...
        (e.g. localhost:8000/api/personal_info/)
        
        Accept Methods: 'GET', 'POST'
        
        If request.method == 'GET':
            (return all the records in the table)

            Response Status:
                200: OK
                others: Bug in the code
            
            Respose Format: (JSON)
                {
                    {
                        record1_column1: ...,
                        record1_column2: ...,
                        ...
                    },
                    {
                        record2_column1: ...,
                        record2_column2: ...,
                        ...
                    },
                    ...
                }
            
        If request.method == 'Post':
            (create new record using the passed data)

            Request Format: (JSON)
            {
                ALL_THE_COLUMNS_IN_TABLE: VALUE
            }

            Response Status:
                201: Created
                400: Creation Failed
            
            Respose Format of 400: (JSON)
            {
            FIELD: [
                "ERROR_MESSAGE"
                ]
            }

    II. path: PATH/<int:id> (e.g. localhost:8000/api/personal_info/3/)
        
        Accept Methods: 'GET', 'PUT', 'DELETE', 'PATCH'

        If request.method == 'GET':
            (Retrieve the record with the id)

            Response Status:
                200: OK
                404: Not Found
            
            Response Formate of 200: (JSON)
                    {
                        record_column1: ...,
                        record_column2: ...,
                        ...
                    }
        If request.method == 'PUT':
            (Update the record with the id)

            Request Format: (JSON)
            {
                ALL_THE_COLUMNS_IN_TABLE: VALUE
            }

            Response Status:
                200: OK
                404: Not Found
                400: Update Failed
        
            Response Format: (JSON)
                The Request JSON

        If request.method == 'DELETE':

            Response Status:
                204: Deleted
                404: Not Found
        If request.method == 'PATCH':
            (similar to PUT but it can do partial update)
"""

class PIViewSet(viewsets.ModelViewSet):
    """
    PATH: http://127.0.0.1:8000/api/personal_information/
    """
    queryset = PersonalInfo.objects.all()
    serializer_class = PISerializer


class MIViewSet(viewsets.ModelViewSet):
    """
    PATH: http://127.0.0.1:8000/api/medical_information/
    """
    queryset = MedicalInfo.objects.all()
    serializer_class = MISerializer

class DIViewSet(viewsets.ModelViewSet):
    """
    PATH: http://127.0.0.1:8000/api/department_information/
    """
    queryset = DepartmentInfo.objects.all()
    serializer_class = DISerializer

class MRViewSet(viewsets.ModelViewSet):
    """
    PATH: http://127.0.0.1:8000/api/medical_record/
    """
    queryset = MedicalRecord.objects.all()
    serializer_class = MRSerializer

    @action(detail=False, methods=['POST'])
    def filter_record(self, request):
        data = JSONParser().parse(request)
        # get rid of NULL values
        for key in data.keys():
            if data[key] is None:
                data.pop(key)
        # print(data)
        # return Response(status=HTTP_200_OK)
        try: 
            q = MedicalRecord.objects.filter(**data).values()
        except MedicalRecord.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)
        else:
            return_data = list(q)[0]
            return_data.update({"record_num":len(return_data)})
            print(return_data)
            return Response(data=return_data, status=HTTP_200_OK)
            # return Response(status=HTTP_200_OK)



