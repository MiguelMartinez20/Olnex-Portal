from django.conf import settings
from django.db import models
from django.utils import timezone

class Employee(models.Model):

    rut = models.CharField(max_length=13)
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    birth_date = models.DateTimeField(blank=True, null=True)
    address = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    salary = models.CharField(max_length=200)


    def publish(self):
        self.date_time = timezone.now()
        self.save()

    def __str__(self):
        return self.rut