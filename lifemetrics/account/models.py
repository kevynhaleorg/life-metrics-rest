from django.db import models

# Create your models here.

class Organization(models.Model):
    name = models.CharField(max_length=50)

class User(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50, default=None)
