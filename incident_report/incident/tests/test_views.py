from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import response
from incident.models import Incident

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.incident_url = reverse('incidents')

    def test_login_GET(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)

    def test_incident_GET(self):
        response = self.client.get(self.incident_url)
        self.assertEquals(response.status_code, 200)

    def test_incident_POST(self):
        response = self.client.post(self.incident_url,{
            'Message': 'test',
            'Position': 100,
            'User': 'admin',
            'Date': '2021-05-20T13:45:00Z'
        })
        self.assertEquals(response.status_code, 201)