from django.db import models

# Create your models here.

class Registration(models.Model):
    user_id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    dob=models.DateField()
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    role=models.CharField(max_length=50)
    otp=models.CharField(max_length=6)
    class Meta:
        db_table = "account"
class Feedback(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=25)
    comment = models.CharField(max_length=2000)
    status = models.CharField(max_length=10)
    class Meta:
        db_table='feedback'