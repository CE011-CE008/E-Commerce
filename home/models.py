from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Registration(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    dob=models.DateField()
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    role=models.CharField(max_length=20)
    class Meta:
         db_table = "account"