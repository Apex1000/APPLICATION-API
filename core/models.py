from django.db import models
from authentication.models import User

STATES = (
      ('UP', 'Worker'),
      ('MP', 'Secretary'),
      ('TP', 'Supervisor'),
      ('DP', 'Admin'),
    )
class Company(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    state = models.CharField(choices=STATES,max_length=50)
    pincode = models.IntegerField()
    def __str__(self):
        return self.name

class Location(models.Model):
    secretary = models.ForeignKey(User,on_delete=models.CASCADE)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    name = models.CharField(max_length=220)
    address = models.CharField(max_length=150)
    state = models.CharField(choices=STATES,max_length=50)
    pincode = models.IntegerField()
    def __str__(self):
        return self.name

class Field(models.Model):
    supervisor = models.ForeignKey(User,on_delete=models.CASCADE)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    name = models.CharField(max_length=220)
    address = models.CharField(max_length=150)
    state = models.CharField(choices=STATES,max_length=50)
    pincode = models.IntegerField()
    def __str__(self):
        return self.name
