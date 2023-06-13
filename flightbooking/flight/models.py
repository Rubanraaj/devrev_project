from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from datetime import datetime

# Create your models here.

class User(AbstractBaseUser):
    first_name = models.CharField(max_length = 64)
    last_name = models.CharField(max_length = 64)
    email = models.CharField(max_length = 64, unique=True)
    phone_num = models.CharField(max_length = 10)
    USERNAME_FIELD = 'email'
    objects = BaseUserManager()
    def __str__(self):
        return f"{self.id}: {self.first_name} {self.last_name}"


class Flight(models.Model):
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    depart_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    duration = models.DurationField(null=True)
    arrival_time = models.DateTimeField(auto_now=True)
    plane = models.CharField(max_length=24)
    airline = models.CharField(max_length=64)
    fare = models.FloatField(null=True)

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    flight = models.ForeignKey(Flight, on_delete = models.DO_NOTHING)
    booking_time = models.DateTimeField(auto_now=True)