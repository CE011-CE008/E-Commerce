from django.db import models

# Create your models here.

class ReceivedProduct(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=200)
    description = models.CharField(max_length=1200)
    price = models.FloatField()
    images = models.ImageField(upload_to='pics/')
    class Meta:
        db_table = 'receivedproduct'
class Cart(models.Model):
    customer_name = models.CharField(max_length=200)
    product_name = models.CharField(max_length=200)
    total = models.IntegerField()
    amount = models.FloatField()