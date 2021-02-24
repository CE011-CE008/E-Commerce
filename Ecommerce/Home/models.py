from django.db import models

# Create your models here.

class Registration(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    dob=models.DateField()
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    role=models.CharField(max_length=50)
    class Meta:
        db_table = "account"