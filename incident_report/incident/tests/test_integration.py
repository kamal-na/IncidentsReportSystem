from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from incident.views import incident, login
from incident.models import Incident
from django.utils import timezone

class TestUrls(SimpleTestCase):
    def test_login_resolve(self):
        url = reverse('login')
        print(resolve(url))
        self.assertEquals(resolve(url).func, login)


    def test_incidents_resolve(self):
        url = reverse('incidents')
        print(resolve(url))
        self.assertEquals(resolve(url).func, incident)


class TestModels(TestCase):

    def create_incident(self, Message="only a test", Position=100, User="Admin"):
        return Incident.objects.create(Message=Message, Position=Position, User= User, Date=timezone.now())

    def test_incident_creation(self):
        w = self.create_incident()
        self.assertTrue(isinstance(w, Incident))

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