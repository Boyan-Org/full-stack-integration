from backend.api.models import Account, Appointment, DepartmentInfo, MedicalRecord, PersonalInfo
from django.http import response
from django.test import TestCase
from rest_framework.test import APIClient

import datetime


class RegisterTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        Account.objects.create(username="userfrank", password="frank", role="patient")

    def test_register(self):
        response = self.client.post(
            '/api/register/',
            {
                "username": "userboyan",
                "password": "boyan",
                "role": "doctor",
                "name": "Boyan Xu"
            },
            format = 'json',
        )
        # print("response_content:", response.content)
        self.assertEqual(response.status_code, 201)

    def test_username_conflict(self):
        response = self.client.post(
            '/api/register/',
            {
                "username": "userfrank",
                "password": "f",
                "role": "patient",
                "name": "F"
            },
            format = 'json',
        )
        self.assertEqual(response.status_code, 409)


class LoginTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        # register
        r = self.client.post(
            '/api/register/',
            {
                "username": "userfrank",
                "password": "frank",
                "role": "patient",
                "name": "Frank Zhou"
            },
            format = 'json',
        )
    def test_login(self):
        response = self.client.post(
            '/api/login/',
            {
                "username": "userfrank",
                "password": "frank",
            },
            format = 'json',
        )
        self.assertEqual(response.status_code, 200)
        # check it returns id
        self.assertIn("id",response.data)


    def test_wrong_username(self):
        response = self.client.post(
            '/api/login/',
            {
                "username": "nobody",
                "password": "frank",
            },
            format = 'json',
        )
        self.assertEqual(response.status_code, 404)
    
    def test_wrong_password(self):
        response = self.client.post(
            '/api/login/',
            {
                "username": "userfrank",
                "password": "nopassword",
            },
            format = 'json',
        )
        self.assertEqual(response.status_code, 401)


class PersonalInfoTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        # create account and personal_info
        self.client.post('/api/register/',{"username": "userfrank","password": "frank","role": "patient","name": "Frank Zhou"},format = 'json',)
        self.id= self.client.post('/api/login/',{"username": "userfrank","password": "frank",},format = 'json',).data["id"]
        self.keys = ["name", "gender", "dateOfBirth", "email", "phoneNumber", "address", "maritalStatus"]
        self.data = {
            "gender":"male",
            "dateOfBirth":"1999-01-26",
            "email":"zz1763@nyu.edu",
            }
    def test_patch_personal_info(self):
        response = self.client.patch("/api/personal_information/"+str(self.id)+"/", self.data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_get_personal_info(self):
        self.test_patch_personal_info()
        response = self.client.get("/api/personal_information/"+str(self.id)+"/")
        self.assertEqual(response.status_code, 200)
        for key in self.keys:
            self.assertContains(response, key)
        for key in self.data:
            self.assertEqual(response.data[key], self.data[key])

class MedicalRecordTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.patient1 = Account.objects.create(username="userfrank", password="frank", role="patient")
        self.patient2 = Account.objects.create(username="useryijian", password="yijian", role="patient")
        self.doctor = Account.objects.create(username="userboyan", password="boyan", role="doctor")
        PersonalInfo.objects.create(id=self.patient1, name = "Frank")
        PersonalInfo.objects.create(id=self.patient2, name = "Yijian")
        PersonalInfo.objects.create(id=self.doctor, name = "Boyan")
        DepartmentInfo.objects.create(id=self.doctor, department = "department1")
        self.record = MedicalRecord.objects.create(
            dateTime="2020-11-30T00:17:34",
            symptoms="good",
            treatments="pills",
            diagnosis="good",
            doctor=self.doctor,
            patient=self.patient2,
            flag=1
        )
    def test_create_medical_record(self):
        response = self.client.post(
            '/api/medical_record/',
            {
                "dateTime":"2020-11-29T00:17:34",
                "symptoms":"s",
                "treatments":"t",
                "diagnosis":"d",
                "doctor":self.doctor.id,
                "patient":self.patient1.id,
                "flag":0
            },
            format = 'json',
            )
        self.assertEqual(response.status_code, 200)
    def test_filter_record(self):
        self.test_create_medical_record()
        response = self.client.post(
            '/api/medical_record/filter_record/',
            {
                "doctor_id": self.doctor.id,
            },
            format='json'
        )
        self.assertEqual(len(response.data.keys()), 2)
        self.assertEqual(len(response.data["record_data"]), 2)

        response = self.client.post(
            '/api/medical_record/filter_record/',
            {
                "symptoms": "s",
            },
            format='json'
        )

        self.assertEqual(len(response.data.keys()), 2)
        self.assertEqual(len(response.data["record_data"]), 1)

    def test_retrieve_medical_record(self):
        self.test_create_medical_record()
        response = self.client.get('/api/medical_record/'+str(self.record.recordID)+'/')
        print(type(response.data))
        self.assertEqual(response.data["attachmentNb"],0)
        self.assertEqual(response.data["dateTime"],datetime.datetime(2020, 11, 30, 0, 17, 34))
        self.assertEqual(response.data["department"],"department1")
        self.assertEqual(response.data["diagnosis"],"good")
        self.assertEqual(response.data["doctor_id"],3)
        self.assertEqual(response.data["doctor_name"],"Boyan")
        self.assertEqual(response.data["flag"],1)
        self.assertEqual(response.data["patient_birthday"],"")
        self.assertEqual(response.data["patient_gender"],"")
        self.assertEqual(response.data["patient_id"],2)
        self.assertEqual(response.data["recordID"],1)
        self.assertEqual(response.data["symptoms"],"good")
        self.assertEqual(response.data["treatments"],"pills")

class AppointmentTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.patient1 = Account.objects.create(username="userfrank", password="frank", role="patient")
        self.patient2 = Account.objects.create(username="useryijian", password="yijian", role="patient")
        self.doctor = Account.objects.create(username="userboyan", password="boyan", role="doctor")
        PersonalInfo.objects.create(id=self.doctor, name = "Boyan")
        DepartmentInfo.objects.create(id=self.doctor, department="department1", supervisor="Hellen", workingHour="[[0,1],[0,0],[1,0],[1,1],[1,1],[0,0],[0,1]]")
        self.appointment = Appointment.objects.create(date=datetime.datetime(2020,12,16), time="morning",submitTime=datetime.datetime(2020,11,28,20,00,00), doctor=self.doctor, patient=self.patient1)
        self.appointment = Appointment.objects.create(date=datetime.datetime(2020,11,29), time="afternoon",submitTime=datetime.datetime(2020,11,28,20,00,00), doctor=self.doctor, patient=self.patient1)

    def test_create_appointment(self):
        response = self.client.post(
            '/api/appointment/',
            {
                "date":"2020-12-09",
                "time": "morning",
                "submitTime":"2020-11-28T22:00:00",
                "doctor":self.doctor.id, 
                "patient":self.patient1.id
            }
        )
        self.assertEqual(response.status_code, 201)
    
    def test_create_too_many_appointments(self):
        response = self.client.post(
            '/api/appointment/',
            {
                "date":"2020-11-29",
                "time": "afternoon",
                "submitTime":"2020-11-28T22:00:00",
                "doctor":self.doctor.id, 
                "patient":self.patient1.id
            }
        )
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.data["error"], "already booked in the slot")

    def test_doctor_not_available(self):
        response = self.client.post(
            '/api/appointment/',
            {
                "date":"2020-12-07",
                "time": "morning",
                "submitTime":"2020-11-28T22:00:00",
                "doctor":self.doctor.id, 
                "patient":self.patient1.id
            }
        )
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.data["error"], "doctor is not available")

    def test_appointment_slot_is_full(self):
        for i in range(10):
            patient = Account.objects.create(username=str(i), password="frank", role="patient")
            Appointment.objects.create(date=datetime.datetime(2020,12,10), time="morning",submitTime=datetime.datetime(2020,11,28,20,00,00), doctor=self.doctor, patient=patient)
        
        response = self.client.post(
            '/api/appointment/',
            {
                "date":"2020-12-10",
                "time": "morning",
                "submitTime":"2020-11-28T22:00:00",
                "doctor":self.doctor.id, 
                "patient":self.patient1.id
            }
        )
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.data["error"], "more than ten appointment in a slot")

    def test_get_available_slots(self):
        response = self.client.post(
            '/api/appointment/get_available_slots/',
            {
                "patient_id":self.patient1.id
            },
            format = 'json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(datetime.date(2020,12,16), response.data["dates"])






        




        


