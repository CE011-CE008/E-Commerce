# Generated by Django 3.1.5 on 2021-03-12 17:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Details',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('description', models.CharField(max_length=10000)),
                ('category', models.CharField(default='Z', max_length=50)),
                ('product_date', models.DateField(default=datetime.date(2021, 3, 12))),
                ('image', models.ImageField(upload_to='pics/')),
            ],
            options={
                'db_table': 'product_details',
            },
        ),
    ]
