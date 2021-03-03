from django.db import models

# Create your models here.

class ReceivedProduct(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=200)
    description = models.CharField(max_length=1200)
    price = models.FloatField()
    images = models.ImageField(upload_to='pics/')
    seller_name=models.CharField(max_length=100)
    seller_email=models.CharField(max_length=100)
    class Meta:
        db_table = 'receivedproduct'
class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    #customer_name = models.CharField(max_length=200)
    # total = models.IntegerField()
    # amount = models.FloatField()
    class Meta:
        db_table = "cart"
class cart_detail(models.Model):
    cart_id=models.CharField(max_length=500)
    product_id=models.CharField(max_length=500)
    items=models.IntegerField()
    class Meta:
        db_table="Cart_details"
