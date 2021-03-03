from django.db import models
from admin_home.models import Product_Details
# Create your models here.

class ReceivedProduct(models.Model):
    id = models.AutoField(primary_key=True)
    seller_name = models.CharField(max_length=100)
    seller_email = models.CharField(max_length=25)
    product_name = models.CharField(max_length=200)
    description = models.CharField(max_length=1200)
    price = models.FloatField()
    images = models.ImageField(upload_to='pics/')
    class Meta:
        db_table = 'receivedproduct'
class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    #customer_name = models.CharField(max_length=200)
    #product_id = models.IntegerField()
    #total = models.IntegerField()
    #amount = models.FloatField()
    class Meta:
        db_table = "cart"
    def __str__(self):
              return self.product_name
class Cart_Details(models.Model):
    cart_id = models.IntegerField()
    product_id = models.IntegerField()
    items  = models.IntegerField()
    class Meta:
        db_table='cart_details'