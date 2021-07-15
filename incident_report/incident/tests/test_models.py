from django.test import TestCase
from django.urls import reverse
from incident.models import Incident
from django.utils import timezone


class TestModels(TestCase):

    def create_incident(self, Message="only a test", Position=100, User="Admin"):
        return Incident.objects.create(Message=Message, Position=Position, User= User, Date=timezone.now())

    def test_incident_creation(self):
        w = self.create_incident()
        self.assertTrue(isinstance(w, Incident))