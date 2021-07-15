from django.test import SimpleTestCase
from django.urls import reverse, resolve
from incident.views import incident, login

class TestUrls(SimpleTestCase):
    def test_login_resolve(self):
        url = reverse('login')
        print(resolve(url))
        self.assertEquals(resolve(url).func, login)


    def test_incidents_resolve(self):
        url = reverse('incidents')
        print(resolve(url))
        self.assertEquals(resolve(url).func, incident)