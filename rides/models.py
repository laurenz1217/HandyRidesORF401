from django.db import models

# Create your models here.


class Person(models.Model):
  name = models.CharField(max_length=64)
  email = models.EmailField()
  origination = models.CharField(max_length=64)  # City
  destination_city = models.CharField(max_length=64)  # City
  destination_state = models.CharField(max_length=2)  # State
  date = models.DateField()
  time = models.TimeField()
  taking_passengers = models.BooleanField(default=True)
  seats_available = models.IntegerField()
  vehicle_type = models.CharField(max_length=64)
