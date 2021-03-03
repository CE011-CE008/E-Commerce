# Generated by Django 3.1.5 on 2021-03-03 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_id', models.IntegerField()),
            ],
            options={
                'db_table': 'cart',
            },
        ),
        migrations.CreateModel(
            name='cart_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_id', models.CharField(max_length=500)),
                ('product_id', models.CharField(max_length=500)),
                ('items', models.IntegerField()),
            ],
            options={
                'db_table': 'Cart_details',
            },
        ),
        migrations.CreateModel(
            name='ReceivedProduct',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1200)),
                ('price', models.FloatField()),
                ('images', models.ImageField(upload_to='pics/')),
                ('seller_name', models.CharField(max_length=100)),
                ('seller_email', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'receivedproduct',
            },
        ),
    ]
