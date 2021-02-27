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
    cart_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    customer_name = models.CharField(max_length=200)
    product_id = models.IntegerField()
    total = models.IntegerField()
    amount = models.FloatField()
    class Meta:
        db_table = "cart"
