# Generated by Django 3.1.5 on 2021-03-19 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admin_home', '0001_initial'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.registration')),
            ],
            options={
                'db_table': 'cart',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=100)),
                ('order_date', models.DateField()),
                ('amount', models.IntegerField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.registration')),
            ],
            options={
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='ReceivedProduct',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('seller_name', models.CharField(max_length=100)),
                ('seller_email', models.CharField(max_length=25)),
                ('product_name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1200)),
                ('price', models.FloatField()),
                ('images', models.ImageField(upload_to='pics/')),
            ],
            options={
                'db_table': 'receivedproduct',
            },
        ),
        migrations.CreateModel(
            name='Order_Details',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('items', models.IntegerField()),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer_home.order')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_home.product_details')),
            ],
            options={
                'db_table': 'order_details',
            },
        ),
        migrations.CreateModel(
            name='Cart_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.IntegerField()),
                ('cart_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer_home.cart')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_home.product_details')),
            ],
            options={
                'db_table': 'cart_details',
            },
        ),
    ]
