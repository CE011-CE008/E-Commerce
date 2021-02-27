from django.db import models

# Create your models here.

class Product_Details(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=200)
    description = models.CharField(max_length=1200)
    price = models.FloatField()
    image = models.ImageField(upload_to='pics/')
    class Meta:
        db_table = 'product_details'