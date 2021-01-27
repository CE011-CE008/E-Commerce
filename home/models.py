from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    dob = models.DateTimeField('date of birth')
    phone=models.CharField(max_length=10)