from django.db import models

# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length=100)
    student_dob = models.DateTimeField('date published')
class BookMaster(models.Model):
    book_id=models.IntegerField(max_length=50)
    book_name=models.CharField(max_length=100)
    book_author=models.CharField(max_length=100)