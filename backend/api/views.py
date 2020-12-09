import json
import datetime
from django.utils.functional import empty
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework import viewsets

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from .models import Account, PersonalInfo, MedicalInfo, DepartmentInfo, MedicalRecord, Appointment
from .serializers import AccountSerializer, PISerializer, DISerializer, MISerializer, MRSerializer, AppSerializer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
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
            data.update({"role": account.role})
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
    try:
        name = data['name']
        role = data['role']
    except:
        return Response(data={"error":"missing register information"}, status=status.HTTP_404_NOT_FOUND)
    serializer = AccountSerializer(data=data)
    if serializer.is_valid():
        account = serializer.save()
        personal_info = PersonalInfo(name=name, id=account)
        if role == 'patient':
            try:
                medical_info = MedicalInfo(id=account)
                medical_info.save()
            except:
                account.delete()
                return Response(data={"error":"fail to auto-create medical_info"}, status=status.HTTP_417_EXPECTATION_FAILED)
        else:
            try:
                dept_info = DepartmentInfo(id=account)
                dept_info.save()
            except:
                account.delete()
                return Response(data={"error":"fail to auto-create dept_info"}, status=status.HTTP_417_EXPECTATION_FAILED)

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

    def create(self, request):
        serializer = MRSerializer(data=request.data)
        if serializer.is_valid():
            record_id = serializer.save().recordID
            return Response(data={"record_id":record_id}, status=status.HTTP_200_OK)
        else:
            return Response(data=request.data, status=status.HTTP_406_NOT_ACCEPTABLE)


    def retrieve(self, request, pk=None):
        """
        Modified ModelViewSet.retrieve()
        Response Json:
            {
                "attachmentNb": 0,
                "dateTime": "2020-11-29T00:17:34",
                "department": "dept1",
                "diagnosis": "d",
                "doctor_id": 2,
                "doctor_name": "Boyan Xu",
                "flag": false,
                "patient_birthday": "",
                "patient_gender": "",
                "patient_id": 1,
                "patient_name": "Frank Zhou",
                "recordID": 1,
                "symptoms": "s",
                "treatments": "t"
            }
        """
        queryset = MedicalRecord.objects.filter(pk=pk).values()
        record_data = list(queryset)
        if len(record_data)==0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            record = record_data[0]
            patient_name = get_person_info(record["patient_id"]).name
            doctor_name = get_person_info(record["doctor_id"]).name
            department = get_department(record["doctor_id"]).department
            patient_gender = get_person_info(record["patient_id"]).gender
            patient_birthday = get_person_info(record["patient_id"]).dateOfBirth
            record.update({
                "patient_name":patient_name,
                "doctor_name":doctor_name,
                "department":department,
                "patient_gender":patient_gender,
                "patient_birthday":patient_birthday,
            })
            return Response(data=record, status=HTTP_200_OK)


    @action(detail=False, methods=['POST'])
    def filter_record(self, request):
        """
        PATH: http://127.0.0.1:8000/api/medical_record/filter_record/
        Method: POST
        Description: return the filtered record that satisfies the requested criteria.
        Request JSON:
            {
                column1: condition1,
                column2: condition2,
                ...
            }
        Response JSON:
            {
                "record_data": [
                    {
                        "dateTime": "2020-11-29T00:17:34",
                        "department": "dept1",
                        "doctor_name": "Boyan Xu",
                        "patient_name": "Frank Zhou",
                        "recordID": 1
                    }
                ],
                "record_num": 1
            }

        """
        data = JSONParser().parse(request)
        # get rid of NULL values
        for key in data.keys():
            if data[key] is None:
                data.pop(key)

        q = MedicalRecord.objects.filter(**data).values()
        record_data = list(q)
        for record in record_data:
            patient_name = get_person_info(record["patient_id"]).name
            doctor_name = get_person_info(record["doctor_id"]).name
            department = get_department(record["doctor_id"]).department
            record.pop("patient_id")
            record.pop("doctor_id")
            record.pop("symptoms")
            record.pop("treatments")
            record.pop("diagnosis")
            record.pop("attachmentNb")
            record.pop("flag")
            record.update({
                "patient_name":patient_name,
                "doctor_name":doctor_name,
                "department": department,
            })
        return_data = {"record_num":len(record_data), "record_data":record_data}
        return Response(data=return_data, status=HTTP_200_OK)


class AppViewSet(viewsets.ModelViewSet):
    """
    PATH: http://127.0.0.1:8000/api/appointment/
    """
    queryset = Appointment.objects.all()
    serializer_class = AppSerializer

    def create(self, request):
        """
        patient book appointment with a doctor.

        Request Json:

            {
                "date":"2020-11-29",
                "time": "morning",
                "submitTime":"2020-11-28T22:00:00",
                "doctor":2,
                "patient":1
            }

        Response status:
            406: Data not acceptable
            409: condition not satisfied (check response.data["error"])
            201: Created
        """
        serializer = AppSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data=request.data, status=status.HTTP_406_NOT_ACCEPTABLE)
        doctor_id = request.data['doctor']
        patient_id = request.data['patient']
        date = request.data['date']
        time = request.data['time']

        workingHour = get_department(doctor_id).workingHour
        if len(workingHour) == 0:
            return Response(data={"error":"doctor working hour missing"}, status=HTTP_404_NOT_FOUND)
        workingHour = json.loads(workingHour)
        date = datetime.datetime.strptime(date, '%Y-%m-%d')
        weekday = date.weekday()
        time_num = 0 if time=='morning' else 1

        # check availability
        if not workingHour[weekday][time_num]:
            return Response(
            data={"error":"doctor is not available"},
            status=status.HTTP_409_CONFLICT
            )

        # check whether too many patients in a slot (maximum 10)
        appointments = Appointment.objects.filter(doctor_id=doctor_id, date=date, time=time)
        if len(list(appointments))>=10:
            return Response(
                    data={"error":"more than ten appointment in a slot"},
                    status=status.HTTP_409_CONFLICT,
                )

        # check whether the patient has made an appointment with the doctor
        appointments.filter(patient_id=patient_id)
        if len(list(appointments))!=0:
            return Response(
                    data={"error":"already booked in the slot"},
                    status=status.HTTP_409_CONFLICT,
                )
        # everything ok then create
        if serializer.is_valid():
            app = serializer.save()
            return Response(data = {"appointment_id":app.appointmentID}, status=status.HTTP_201_CREATED)
        return Response(data=request.data, status=status.HTTP_406_NOT_ACCEPTABLE)

    @action(detail=False, methods=['POST'])
    def filter_appointment(self, request):
        """
        PATH: http://127.0.0.1:8000/api/appointment/filter_appointment/
        Method: POST
        Description: return the filtered appointment that satisfies the requested criteria.
        Request JSON:
            {
                column1: condition1,
                column2: condition2,
                ...
            }
        Response JSON:
                {
                    "record_data": [
                        {
                            "appointmentID": 2,
                            "date": "2020-12-02",
                            "department": "dept1",
                            "doctor_id": 2,
                            "doctor_name": "Boyan Xu",
                            "patient_id": 1,
                            "patient_name": "Frank Zhou",
                            "submitTime": "2020-11-28T22:00:00",
                            "time": "morning"
                        }
                    ],
                    "record_num": 1
                }
        """
        data = JSONParser().parse(request)
        # get rid of NULL values
        for key in data.keys():
            if data[key] is None:
                data.pop(key)
        q = Appointment.objects.filter(**data).values()
        record_data = list(q)
        for record in record_data:
            dept = get_department(record["doctor_id"]).department
            patient_name = get_person_info(record["patient_id"]).name
            doctor_name = get_person_info(record["doctor_id"]).name
            record.update({
                "department":dept,
                "patient_name":patient_name,
                "doctor_name":doctor_name,
            })

        return_data = {"record_num":len(record_data), "record_data":record_data}
        return Response(data=return_data, status=HTTP_200_OK)

    @action(detail=False, methods=['POST'])
    def get_available_slots(self, request):
        """
        PATH: http://127.0.0.1:8000/api/appointment/get_available_slots/
        Note:
            The slot is available if and only if:
                1). The doctor works at that slot
                2). There are less than 10 people book the slot with the doctor
                3). The patient has not booked the slot with the doctor
        Request Json:
            {
                "patient_id": 1,
            }
        Response Json:
            {
                "dates": [
                    "2020-12-14",
                    "2020-12-11",
                    "2020-12-07",
                    "2020-12-17",
                    "2020-12-04",
                    "2020-12-13",
                    "2020-12-10",
                    "2020-12-09",
                    "2020-12-06",
                    "2020-12-16"
                ],
                "dept_names": [
                    "dept2",
                    "dept1"
                ],
                "doctor_names": [
                    "Hellen Wang",
                    "Boyan Xu"
                ],
                "slots": [
                    {
                        "date": "2020-12-04",
                        "department": "dept1",
                        "doctor_id": 2,
                        "doctor_name": "Boyan Xu",
                        "time": "morning"
                    },
                    ...,
                    ...,
                    {
                        "date": "2020-12-17",
                        "department": "dept1",
                        "doctor_id": 2,
                        "doctor_name": "Boyan Xu",
                        "time": "afternoon"
                    },
                    {
                        "date": "2020-12-04",
                        "department": "dept2",
                        "doctor_id": 3,
                        "doctor_name": "Hellen Wang",
                        "time": "morning"
                    },
                    ...,
                    ...,
                    {
                        "date": "2020-12-17",
                        "department": "dept2",
                        "doctor_id": 3,
                        "doctor_name": "Hellen Wang",
                        "time": "afternoon"
                    }
                ],
                "times": [
                    "morning",
                    "afternoon"
                ]
            }
        """
        data = JSONParser().parse(request)
        if "patient_id" not in data:
            return Response(data={"error":"patient identity missing"}, status=HTTP_404_NOT_FOUND)
        # list all the slots filtered by workingHour
        dept_infos = DepartmentInfo.objects.all()
        slots = []
        for dept_info in dept_infos:
            slots += two_week_working_hour(dept_info)

        i = 0
        while i < len(slots):
            slot = slots[i]
            doctor_id = slot["doctor_id"]
            date = slot["date"]
            time = slot["time"]
            appointments = Appointment.objects.filter(doctor_id=doctor_id, date=date, time=time)
            # filter the slots by maximum number of appointments
            if len(list(appointments))>=10:
                i-=1
                slots.remove(slot)
                continue
            # filter the slots by whether the patient has booked an appointment with the doctor
            appointments.filter(patient_id=data["patient_id"])
            if len(list(appointments))!=0:
                i-=1
                slots.remove(slot)
            i+=1
        # extract the unique information
        dept_names = list(set([slot["department"] for slot in slots]))
        doctor_names = list(set([slot["doctor_name"] for slot in slots]))
        dates = list(set([slot["date"] for slot in slots]))
        times = list(set([slot["time"] for slot in slots]))
        return_data = {
            "dept_names": dept_names,
            "doctor_names": doctor_names,
            "dates": dates,
            "times": times,
            "slots": slots,
        }
        return Response(data=return_data, status=status.HTTP_200_OK)

# Assistant Functions
def get_person_info(id):
    """
    convert id to PersonalInfo.name
    """
    try:
        info = PersonalInfo.objects.get(id=id)
    except PersonalInfo.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)
    else:
        return info

def get_department(id):
    """
    convert id to DepartmentInfo.department
    """
    try:
        info = DepartmentInfo.objects.get(id=id)
    except DepartmentInfo.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)
    else:
        return info

def two_week_working_hour(dept_info):
    """
    convert workingHour into two week's everyday slot
    """
    today = datetime.datetime.today()
    weekday = today.weekday()
    workingHour = json.loads(dept_info.workingHour)

    schedule = []
    for i in range(14):
        if workingHour[(weekday+i+1)%7][0]:
            schedule.append({
                "date": (today+datetime.timedelta(days=i+1)).date(),
                "time": "morning",
                "doctor_id": dept_info.id.id,
                "doctor_name": get_person_info(dept_info.id.id).name,
                "department": dept_info.department,
            })
        if workingHour[(weekday+i+1)%7][1]:
            schedule.append({
                "date": (today+datetime.timedelta(days=i+1)).date(),
                "time": "afternoon",
                "doctor_id": dept_info.id.id,
                "doctor_name": get_person_info(dept_info.id.id).name,
                "department": dept_info.department,
            })
    return schedule


