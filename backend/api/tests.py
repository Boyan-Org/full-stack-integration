from backend.api.models import Account
from django.http import response
from django.test import TestCase
from rest_framework.test import APIClient

class RegisterTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_register(self):
        response = self.client.post(
            '/api/register/',
            {
                "username": "userfrank",
                "password": "frank",
                "role": "patient",
                "name": "Frank Zhou"
            },
            format = 'json',
        )
        # print("response_content:", response.content)
        self.assertEqual(response.status_code, 201)

    def test_username_conflict(self):
        self.client.post(
            '/api/register/',
            {
                "username": "userfrank",
                "password": "frank",
                "role": "patient",
                "name": "Frank Zhou"
            },
            format = 'json',
        )
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
        # create account and personal_info
        self.client.post(
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

    def test_wrong_username(self):
        response = self.client.post(
            '/api/login/',
            {
                "username": "userfrank",
                "password": "frank",
            },
            format = 'json',
        )
        self.assertEqual(response.status_code, 200)


# class PersonalInfoTestCase(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         Account.objects.create(
#             username = "userfrank",
#             password = "frank",
#             role = "patient",
#         )
#     def test_login(self):
#         response = self.client.post(
#             '/api/login/',
#             {
#                 "username": "userfrank",
#                 "password": "frank",
#             }
#         )
#         print(response.content) 
#         self.assertEqual(response.status_code, 200)


