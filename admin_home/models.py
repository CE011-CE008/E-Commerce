from django.db import models

# Create your models here.
class Product_details(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    price=models.FloatField()
    description=models.CharField(max_length=10000)
    category=models.CharField(default="Z",max_length=50)
    product_date=models.DateField()
    class Meta:
        db_table="product_details"

