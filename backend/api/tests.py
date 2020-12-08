from backend.api.models import Account
from django.http import response
from django.test import TestCase, Client

# class RegisterTestCase(TestCase):
#     def setUp(self):
#         self.client = Client()

#     def test_register(self):
#         response = self.client.post(
#             '/api/register/',
#             data = {
#                     "username": "userfrank",
#                     "password": "frank",
#                     "role": "patient",
#                     "name": "Frank Zhou"
#                     },
#         )
#         print(response.content)
#         self.assertEqual(response.status_code, 201)


class LoginTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        Account.objects.create(
            username = "userfrank",
            password = "frank",
            role = "patient",
        )
    def test_login(self):
        response = self.client.post(
            '/api/login/',
            {
                "username": "userfrank",
                "password": "frank",
            }
        )
        print(response.content) 
        self.assertEqual(response.status_code, 200)



