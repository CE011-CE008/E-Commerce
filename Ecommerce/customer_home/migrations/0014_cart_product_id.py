# Generated by Django 3.1.5 on 2021-02-26 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_home', '0013_auto_20210226_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='product_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
