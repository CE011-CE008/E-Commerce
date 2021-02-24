# Generated by Django 3.1.5 on 2021-02-24 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Details',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1200)),
                ('price', models.FloatField()),
            ],
            options={
                'db_table': 'product_details',
            },
        ),
    ]
