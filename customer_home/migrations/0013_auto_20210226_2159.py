# Generated by Django 3.1.5 on 2021-02-26 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_home', '0012_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='id',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='product_name',
        ),
        migrations.AddField(
            model_name='cart',
            name='cart_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='customer_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='cart',
            table='cart',
        ),
    ]
