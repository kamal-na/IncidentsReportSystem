from django.db import models

class Incident(models.Model):
    Message = models.CharField(max_length=100)
    Position = models.IntegerField()
    User = models.CharField(max_length=100)
    Date = models.DateTimeField()


